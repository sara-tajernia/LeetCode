from collections import Counter

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        saved = []
        current = []

        for letter in s:
            if letter in current:
                if len(saved) < len(current):
                    saved = current[:]
                index = current.index(letter)
                current = current[index + 1:]
            current.append(letter)

        return max(len(current), len(saved))

        
        
    def findMedianSortedArrays(self, nums1, nums2):
        counter1 = 0
        counter2 = 0
        for _ in range(int((len(nums1) + len(nums2))/2 - 0.5)):
            if nums1[counter1] < nums2[counter2]:
                counter1 += 1
            else:
                counter2 += 1

        if (len(nums1) + len(nums2)) % 2 == 0:
            return  (nums1[counter1] + nums2[counter2])/2
        else:
            return nums1[counter1] if nums1[counter1] < nums2[counter2] else nums2[counter2]
 
        
    def reverse(self, x):
        result = 0
        num = abs(x)
        while 9 < num:
            result = result*10 + num % 10
            num //=10
        result = result*10 + num % 10
        if x < 0:
            result = -result

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
    
    def isUgly(self, n):
        if n == 0:
            return False
        for i in [2,3,5]:
            while n % i == 0:
                n /=i
        return n==1

    def addBinary(self, a, b):
        max_len = max(len(a), len(b))
        a = list(map(int, a.zfill(max_len)))
        b = list(map(int, b.zfill(max_len)))
        
        carry = 0
        result = []

        for i in range(len(a)-1, -1, -1):
            if (a[i] + b[i] + carry) % 2 == 1:
                result.append(1)
            else:
                result.append(0)

            if 1 < a[i] + b[i] + carry:
                carry = 1
            else:
                carry = 0

        if carry == 1:
            result.append(carry)
        return  ''.join(map(str, result[::-1])) 
    
    def lengthOfLastWord(self, s):
        s = list(s)
        counter = 0
        i = len(s) -1
        while s[i] == ' ':
            s.pop(-1)
            i -= 1
        i = len(s) -1
        while s[i] != ' ':
            counter += 1
            i -= 1
            if i == -1:
                break
        return counter
    
    def largestInteger(self, nums, k):
        numFirst = nums[0]
        numLast = nums[-1]
        
        if k == len(nums):
            return max(nums)
        
        if k == 1:
            count = Counter(nums)
            unique_numbers = [num for num, freq in count.items() if freq == 1]
            return max(unique_numbers) if unique_numbers else -1

        
        for i in range(len(nums)):
            if nums[i] == numFirst and i != 0:
                numFirst = -1
            elif nums[i] == numLast and i != len(nums)-1:
                numLast = -1
    
        if numFirst < numLast:
            return numLast
        else:
            return numFirst
        
    def climbStairs(self, n):
        if n == 1:
            return 1
        
        num1 = 1
        num2 = 2
        for i in range(2, n):
            swap = num2
            num2 += num1
            num1 = swap
            
        return num2
    
    # def threeSum(self, nums):
    #     answer = []
    #     print(nums)
    #     twoSum = {}
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             print(twoSum, nums[i], nums[j])
    #             for n in twoSum.keys():
    #                 if -nums[j] == n:
    #                     for val in twoSum[n]:
    #                         print('hiiiii', nums[j], val)

    #                         three = tuple(sorted((val[0], val[1], nums[j])))
    #                         if three not in answer:
    #                             answer.append(three)
    #                             print(answer, 'added')
                        

    #             pair = tuple(sorted((nums[i], nums[j])))
    #             if nums[i] + nums[j] in twoSum:
    #                 if pair not in twoSum[nums[i] + nums[j]]:
    #                     twoSum[nums[i] + nums[j]].append(pair)
    #             else:
    #                 twoSum[nums[i] + nums[j]] = [pair]

    #     return answer

    def maxWidthOfVerticalArea(self, points):
        max = 0
        xs = []
        for i in range(len(points)):
            xs.append(points[i][0])
        xs.sort()
        for i in range(len(xs)-1):
            if max < abs(xs[i] - xs[i+1]):
                max = abs(xs[i] - xs[i+1])
        return max
    

if __name__ == "__main__":
    Solution = Solution()
    # print(Solution.lengthOfLongestSubstring(s = "pwwkew"))
    # print(Solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])) 
    # print(Solution.reverse(x = 1534236469))
    # print(Solution.isUgly(n=14))
    # print(Solution.addBinary(a = "1111", b = "1111"))
    # print(Solution.lengthOfLastWord(s = "luffy is still joyboy"))
    # print(Solution.largestInteger(nums=[0,0], k=1))
    # print(Solution.climbStairs(n = 1))
    # print(Solution.threeSum(nums = [1,2,-2,-1]))
    print(Solution.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
