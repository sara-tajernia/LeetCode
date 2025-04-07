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


if __name__ == "__main__":
    Solution = Solution()
    # print(Solution.lengthOfLongestSubstring(s = "pwwkew"))
    # print(Solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])) 
    # print(Solution.reverse(x = 1534236469))
    print(Solution.isUgly(n=14))
