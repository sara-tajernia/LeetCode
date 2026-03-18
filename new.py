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
    
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

        
    def isSubsequence(self, s, t):
        for i in s:
            if i in t:
                t = t[t.index(i)+1:]
                print(t)
            else:
                return False
        return True

    def hammingWeight(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


s = Solution()
# print(s.missingNumber([3,0,1]))
# print(s.firstUniqChar("loveleetcode"))
# print(s.isPerfectSquare(15))
# print(s.intersection([4,9,5], [9,4,9,8,4]))
# print(s.isSubsequence(s = "axc", t = "ahbgdc"))
# print(s.rob(nums = [2,7,9,3,1]))
print(s.hammingWeight(11))
