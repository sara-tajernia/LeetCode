import math

class Solution(object):
    # [9,6,4,2,3,5,7,0,1] -> 8
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def firstUniqChar(self, s):
        letters = {}
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        for i, char in enumerate(s):
            if letters[char] == 1:
                return i
        return -1
    
    def isPerfectSquare(self, num):
        if num<0:
            return False
        sq = math.sqrt(num)
        return sq.is_integer()
        
        


s = Solution()
# print(s.missingNumber([3,0,1]))
# print(s.firstUniqChar("loveleetcode"))
print(s.isPerfectSquare(15))
