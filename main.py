class Solution(object):
    def lengthOfLongestSubstring(self, s):
        saved = []
        max_length = []
        for letter in s:
            check = True
            for i in range(len(max_length)):
                if letter == max_length[i]:
                    check = False
                    break
            if not check:
                if len(saved) < len(max_length):
                    saved = max_length
                max_length = max_length[i+1::]
            max_length.append(letter)

        return max(len(max_length), len(saved))


        
        
        



if __name__ == "__main__":
    Solution = Solution()
    print(Solution.lengthOfLongestSubstring(s = "pwwkew"))