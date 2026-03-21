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
            print(n)
            n >>= 1
        return count
    
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
    
    def reverseWords(self, s):
        x = s.split()[::-1]
        return ' '.join(x)
    
    def maxProduct(self, nums):
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, num * max_so_far, num * min_so_far)
            temp_min = min(num, num * max_so_far, num * min_so_far)

            max_so_far = temp_max
            min_so_far = temp_min

            result = max(result, max_so_far)
        return result
    
    def findMin(self, nums):
        first = 0
        mid = len(nums)//2
        end = len(nums)-1
        while True:
            if nums[mid] <= nums[end]:
                end = mid
                mid = (first+end)//2
            elif nums[first] <= nums[mid]:
                print(nums[mid], nums[end])
                first = mid
                mid = (first+end)//2
            if end == mid or first == mid:
                return min(nums[first], nums[end])










s = Solution()
# print(s.missingNumber([3,0,1]))
# print(s.firstUniqChar("loveleetcode"))
# print(s.isPerfectSquare(15))
# print(s.intersection([4,9,5], [9,4,9,8,4]))
# print(s.isSubsequence(s = "axc", t = "ahbgdc"))
# print(s.rob(nums = [2,7,9,3,1]))
# print(s.hammingWeight(11))
# print(s.reverseWords("the sky is blue"))
# print(s.maxProduct([2,3,-2,4]))
print(s.findMin([1,2]))


