

# def solveMeFirst(a,b):
# 	return a+b


# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)



import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        return n * extraLongFactorials(n-1)

if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))