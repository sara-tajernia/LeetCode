# import asyncio
# import websockets
# import sounddevice as sd
# import numpy as np
# import json

# # ----- تنظیمات -----
# API_KEY ="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"
# MODEL = "gpt-4o-realtime-preview-2024-12-17"  # نسخه مدل
# SAMPLE_RATE = 16000
# CHANNELS = 1
# BLOCKSIZE = 1024


# async def run_realtime():
#     uri = f"wss://api.openai.com/v1/realtime?model={MODEL}"

#     async with websockets.connect(
#         uri,
#         subprotocols=["realtime"],   # ✅ حتما باشه
#         additional_headers=[
#             ("Authorization", f"Bearer {API_KEY}"),
#             ("OpenAI-Beta", "realtime=v1"),
#         ],
#     ) as ws:

#         print("🔊 وصل شدی! حالا صحبت کن...")

#         loop = asyncio.get_running_loop()

#         def callback(indata, frames, time, status):
#             if status:
#                 print("⛔ مشکل ضبط:", status)
#             audio_bytes = indata.tobytes()
#             fut = asyncio.run_coroutine_threadsafe(
#                 ws.send(json.dumps({
#                     "type": "input_audio_buffer.append",
#                     "audio": audio_bytes.hex()
#                 })),
#                 loop
#             )
#             try:
#                 fut.result()
#             except Exception as e:
#                 print("❌ خطای ارسال:", e)

#         stream = sd.InputStream(
#             callback=callback,
#             channels=CHANNELS,
#             samplerate=SAMPLE_RATE,
#             blocksize=BLOCKSIZE,
#             dtype='int16'
#         )
#         stream.start()

#         async for message in ws:
#             event = json.loads(message)

#             if event["type"] == "response.output_audio.delta":
#                 audio = bytes.fromhex(event["audio"])
#                 audio_array = np.frombuffer(audio, dtype=np.int16)
#                 sd.play(audio_array, samplerate=SAMPLE_RATE)
#                 sd.wait()

#             elif event["type"] == "response.completed":
#                 print("\n🤖 پاسخ کامل شد\n")


# if __name__ == "__main__":
#     asyncio.run(run_realtime())



# example requires websocket-client library:
# pip install websocket-client




# import os
# import json
# import websocket

# OPENAI_API_KEY ="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"

# url = "wss://api.openai.com/v1/realtime?model=gpt-realtime"
# headers = ["Authorization: Bearer " + OPENAI_API_KEY]


# def on_open(ws):
#     print("Connected to server.")


# def on_message(ws, message):
#     data = json.loads(message)
#     print("Received event:", json.dumps(data, indent=2))


# ws = websocket.WebSocketApp(
#     url,
#     header=headers,
#     on_open=on_open,
#     on_message=on_message,
# )

# ws.run_forever()


import websocket
import json
import base64
import sounddevice as sd
import numpy as np
import threading

OPENAI_API_KEY ="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"
URL = "wss://api.openai.com/v1/realtime?model=gpt-realtime"

headers = [
    "Authorization: Bearer " + OPENAI_API_KEY,
    "OpenAI-Beta: realtime=v1",
]

# تنظیمات صوت
SAMPLE_RATE = 24000
BLOCK_SIZE = 1024

# --- فرستادن صدا از میکروفون ---
def record_and_send(ws):
    def callback(indata, frames, time, status):
        if status:
            print(status)
        # تبدیل به PCM 16bit و سپس base64
        pcm_data = (indata[:, 0] * 32767).astype(np.int16).tobytes()
        b64 = base64.b64encode(pcm_data).decode("utf-8")
        ws.send(json.dumps({"type": "input_audio_buffer.append", "audio": b64}))

    # استریم از میکروفون
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=callback, blocksize=BLOCK_SIZE):
        print("🎙️ در حال ضبط صدا... صحبت کن (Ctrl+C برای خروج)")
        while True:
            sd.sleep(1000)


# --- گرفتن پیام‌ها از سرور ---
def on_message(ws, message):
    data = json.loads(message)

    # متن زنده
    if data.get("type") == "response.output_text.delta":
        print("💬", data["delta"], end="", flush=True)

    # صدا زنده
    if data.get("type") == "response.output_audio.delta":
        audio_chunk = base64.b64decode(data["delta"])
        audio_array = np.frombuffer(audio_chunk, dtype=np.int16).astype(np.float32) / 32767.0
        sd.play(audio_array, SAMPLE_RATE)

    # پایان پاسخ
    if data.get("type") == "response.completed":
        print("\n✅ پاسخ کامل شد")


def on_open(ws):
    print("✅ Connected to server.")
    # شروع ضبط و ارسال صدا در یک thread جدا
    threading.Thread(target=record_and_send, args=(ws,), daemon=True).start()


def on_error(ws, error):
    print("❌ Error:", error)


def on_close(ws, close_status_code, close_msg):
    print("🔌 Connection closed.")


if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        URL,
        header=headers,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws.run_forever()





# import websocket
# import json

# OPENAI_API_KEY ="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"
# URL = "wss://api.openai.com/v1/realtime?model=gpt-realtime"
# headers = ["Authorization: Bearer " + OPENAI_API_KEY]

# def on_open(ws):
#     print("✅ Connected to server.")

# def on_message(ws, message):
#     data = json.loads(message)
#     print("Received:", data)

# ws = websocket.WebSocketApp(URL, header=headers, on_open=on_open, on_message=on_message)
# ws.run_forever()


