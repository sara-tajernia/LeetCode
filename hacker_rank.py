

# def solveMeFirst(a,b):
# 	return a+b


# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)



# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'extraLongFactorials' function below.
# #
# # The function accepts INTEGER n as parameter.
# #

# def extraLongFactorials(n):
#     if n == 1:
#         return 1
#     else:
#         return n * extraLongFactorials(n-1)

# if __name__ == '__main__':
#     n = int(input().strip())

#     print(extraLongFactorials(n))













# def queensAttack(n, k, r_q, c_q, obstacles):
#     obstacles = set(tuple(x) for x in obstacles)
#     counter = 0

#     # right
#     for i in range(c_q+1, n+1):
#         if (r_q, i) in obstacles:
#             break
#         counter += 1

#     # left
#     for i in range(c_q-1, 0, -1):
#         if (r_q, i) in obstacles:
#             break
#         counter += 1

#     # up
#     for i in range(r_q+1, n+1):
#         if (i, c_q) in obstacles:
#             break
#         counter += 1

#     # down
#     for i in range(r_q-1, 0, -1):
#         if (i, c_q) in obstacles:
#             break
#         counter += 1

#     # diagonals
#     x, y = r_q, c_q
#     while x < n and y < n:
#         x += 1
#         y += 1
#         if (x, y) in obstacles:
#             break
#         counter += 1

#     x, y = r_q, c_q
#     while x > 1 and y > 1:
#         x -= 1
#         y -= 1
#         if (x, y) in obstacles:
#             break
#         counter += 1

#     x, y = r_q, c_q
#     while x > 1 and y < n:
#         x -= 1
#         y += 1
#         if (x, y) in obstacles:
#             break
#         counter += 1

#     x, y = r_q, c_q
#     while x < n and y > 1:
#         x += 1
#         y -= 1
#         if (x, y) in obstacles:
#             break
#         counter += 1

#     return counter


# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     r_q, c_q = map(int, input().split())

#     obstacles = [list(map(int, input().split())) for _ in range(k)]

#     result = queensAttack(n, k, r_q, c_q, obstacles)
#     print(result)









# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# def chocolateInBox(arr):
#     total_xor = 0
#     for num in arr:
#         total_xor ^= num

#     if total_xor == 0:
#         return 0

#     count = 0
#     for num in arr:
#         target = num ^ total_xor
#         if target < num:
#             count += 1

#     return count


    

# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = chocolateInBox(arr)
#     print(result)
#     # fptr.write(str(result) + '\n')

#     # fptr.close()





#!/bin/python3

import math
import os
import random
import re
import sys


def nimGame(pile):
    total_xor = 0
    for num in pile:
        total_xor ^= num
    if total_xor == 0:
        return "Second"
    return "First"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)
        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
