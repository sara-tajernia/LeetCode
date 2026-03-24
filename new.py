import math
import heapq
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
            

    def repeatedStringMatch(self, a, b):
        if b in a:
            return 1
        count = 1
        ap = a
        while len(ap) <= len(b) + 2*len(a):
            print(ap, b, a, len(ap), len(b), len(a))
            print(b , ap)
            if b in ap:
                return count
            ap = ap+a
            # print(ap)
            count += 1 
        return -1

    def maxKelements(self, nums, k):
        nums = [-x for x in nums]
        # print(nums) 
        heapq.heapify(nums)
        # print(nums, "\n")
        score = 0
        for _ in range(k):
            x = -heapq.heappop(nums)
            print(x)
            score += x
            heapq.heappush(nums, -((x + 2) // 3))

        return score
    
    def minStoneSum(self, piles, k):
        piles = [-p for p in piles]
        heapq.heapify(piles)
        score = 0
        for _ in range(k):
            num = -heapq.heappop(piles)
            # print(num)
            score += num
            heapq.heappush(piles, -((num+1)//2))
            # print(piles)

        return -sum(piles)
    

    def moveZeroes(self, nums):
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                size -= 1
                i -= 1
            i += 1

        return nums
    
    def passThePillow(self, n, time):
        if ((time-1) // (n-1)) % 2 == 0:
            # print('sfdsf')
            return (time-1) % (n-1) + 2
        else:
            return n - (time-1) % (n-1) -1







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
# print(s.findMin([1,2]))
# print(s.repeatedStringMatch(a = "abc", b = "cabcabca"))
# print(s.maxKelements(nums = [1,10,3,3,3], k = 3))
# print(s.minStoneSum(piles = [4,3,6,7], k = 3))
# print(s.moveZeroes([0,0,1]))
# print(s.passThePillow(n = 3, time = 2))
print(s.passThePillow(n = 18, time = 38))

print(37//17)
