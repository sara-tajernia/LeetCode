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


    # def combinationSum4(self, nums, target):
    #     dp = [0] * (target + 1)
    #     dp[0] = 1
    #     for i in range(1, target + 1):
    #         for num in nums:
    #             if num <= i:
    #                 print(dp[i] , dp[i - num], num, i)
    #                 dp[i] += dp[i - num]
    #             print(dp)
    #         print("\n")
    #     return dp[target]

    # def kthSmallest(self, matrix, k):
    #     print()
        # count = 0
        # xi, yi, xj, yj = 0,0,0,0
        # size = len(matrix)
        # while count <= k:
        #     print(matrix[xi][yi], matrix[xj][yj])
        #     if matrix[xi][yi] < matrix[xj][yj]:
        #         n = (yi * size) + xi + 1
        #         print("intial i", xi, yi)
        #         yi = n // size
        #         xi = n % size
        #         print("changed i", xi, yi)
        #     else: 
        #         n = (xj * size) + yj + 1
        #         print("intial j", xj, yj)
        #         xj = n // size
        #         yj = n % size
        #         print("changed j", xj, yj)
        #     print('\n')
        #     count += 1
            


    def removeTrailingZeros(self, num):
        num = str(num)
        i = len(num) - 1
        while i >= 0 and num[i] == '0':
            i -= 1
        return num[:i+1]
    
    # def findMissingElements(self, nums):
    #     s = sorted(nums)
    #     miss = []
    #     add = s[0]
    #     print('sdfdf', add, s[len(s)-1]-add)
    #     # for i in range(s[len(s)-1]-add):
    #         # print(i+add, s[i])
    #     i = 0
    #     while i <= s[len(s)-1]-add:
    #         print(i)
    #         if i+ add != s[i]:
    #             miss.append(i+add)
    #             print(i+add, s[i])
    #         else:
    #             print("No missing element for", i+add)
    #         i += 1



    def findMissingElements(self, nums):
        s = sorted(nums)
        miss = []
        add = s[0]
        index = 0
        for i in range(s[-1] - s[0] + 1):
            if s[index] != i+add:
                miss.append(i+add)
            else:
                index += 1
        return miss


    # def maxProduct(self, nums):
    #     n = 100000
    #     if 0 in nums:
    #         i = nums.index(0)
    #         nums[i] = n
    #     else:
    #         i = nums.index(min(nums, key=abs))
    #         nums[i] = n
    #     product = 1
    #     top3 = sorted(nums, key=abs, reverse=True)[:3]

    #     product = top3[0] * top3[1] * top3[2]
    #     return abs(product)



    def maxProduct(self, nums):
        top3 = sorted(nums, key=abs, reverse=True)[:2]
        return abs(top3[0] * top3[1] * 100000)


    def checkStrings(self, s1, s2):
        evens_s1, odds_s1 = [], []
        evens_s2, odds_s2 = [], []
        for i in range(len(s1)):
            if i % 2 == 0:
                evens_s1.append(s1[i])
            else:
                odds_s1.append(s1[i])

        for i in range(len(s2)):
            if i % 2 == 0:
                evens_s2.append(s2[i])
            else:
                odds_s2.append(s2[i])
        if sorted(evens_s1) == sorted(evens_s2) and sorted(odds_s1) == sorted(odds_s2):
            return True
        return False
        

    def maxSum(self, nums, m, k):
        
        def almost_unique(l):
            unique = {}
            for n in l:
                if n in unique:
                    unique[n] += 1
                else:
                    unique[n] = 1
            # print(len(unique) >= m)
                if len(unique) >= m:
                    return sum(l)
            return 0
        
        result = 0
        for i in range(len(nums)-k+1):
            # print(nums[i:i+k])
            x = almost_unique(nums[i:i+k])
            if result < x:
                result = x
        
        return result

    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                if val == ".":
                    continue

                # box index (important!)
                box_index = (i // 3) * 3 + (j // 3)

                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)

        return True


    # def solveSudoku(self, board):
    #     # rows = [set() for _ in range(9)]
    #     # cols = [set() for _ in range(9)]
    #     # boxes = [set() for _ in range(9)]
    #     rows = [{i:set()} for i in range(1, 10)]
    #     cols = [{i:set()} for i in range(1, 10)]
    #     boxes = [{i:set()} for i in range(1, 10)]

    #     for i in range(9):
    #         for j in range(9):
    #             val = board[i][j]

    #             if val == ".":
    #                 continue

    #             box_index = (i // 3) * 3 + (j // 3)
    #             print(rows[i])
    #             # rows[i].add(val)
    #             # cols[j].add(val)
    #             # boxes[box_index].add(val)
    #     # print(rows)
    #     print(cols)


    def countAndSay(self, num):
        def sequence(n):
            counter = 1
            res = ''
            for i in range(1, len(n)):
                if n[i] == n[i-1]:
                    counter += 1
                else:
                    res += str(counter) + str(n[i-1])
                    counter = 1
            res += str(counter) + str(n[-1])
            return res
        
        res = "1"
        for _ in range(int(num)-1):
            res = sequence(res)
        return res
    
    def checkString(self, s):
        check = True
        for i in s:
            if i == "b":
                check = False
            if not check and i == 'a':
                return False
        return True
    
    def numberOfBeams(self, bank):
        counter = 0
        last_ones = bank[0].count('1')
        for i in range(1, len(bank)):
            ones = bank[i].count('1')
            # print(ones)
            if ones != 0:
                counter += ones*last_ones
                last_ones = ones
                # print("up", last_ones, counter)
        return counter







        
s = Solution()
# print(s.missingNumber([3,0,1]))
# print(s.firstUniqChar("loveleetcode"))
# print(s.isPerfectSquare(15))
# print(s.intersection([4,9,5], [9,4,9,8,4]))
# print(s.isSubsequence(s = "axc", t = "ahbgdc"))
# print(s.rob(nums = [2,7,9n,3,1]))
# print(s.hammingWeight(11))
# print(s.reverseWords("the sky is blue"))
# print(s.maxProduct([2,3,-2,4]))
# print(s.findMin([1,2]))
# print(s.repeatedStringMatch(a = "abc", b = "cabcabca"))
# print(s.maxKelements(nums = [1,10,3,3,3], k = 3))
# print(s.minStoneSum(piles = [4,3,6,7], k = 3))
# print(s.moveZeroes([0,0,1]))
# print(s.passThePillow(n = 3, time = 2))
# print(s.passThePillow(n = 18, time = 38))
# print(s.combinationSum4(nums = [1,2,3], target = 4))               377
# print(s.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
# print(s.kthSmallest(matrix = [[1,2],[1,3]], k = 2))
# print(s.removeTrailingZeros(5100230100))
# print(s.findMissingElements(nums = [7,8,6,9,12]))
# print(s.findMissingElements(nums = [1,4,2,5, 3]))
# print(s.maxProduct(nums = [-4,-2,-1,-3]))
# print(s.minMovesToMakePalindrome(s = "letelt"))
# print(s.checkStrings(s1 = "abcde", s2 = "baedc"))
# print(s.checkStrings(s1 = "abcdba", s2 = "cabdab"))
# print(s.maxSum(nums = [1], m = 1, k = 1))
# print(s.isValidSudoku(board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))
# print(s.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],
#                              ["6",".",".","1","9","5",".",".","."],
#                              [".","9","8",".",".",".",".","6","."],
#                              ["8",".",".",".","6",".",".",".","3"],
#                              ["4",".",".","8",".","3",".",".","1"],
#                              ["7",".",".",".","2",".",".",".","6"],
#                              [".","6",".",".",".",".","2","8","."],
#                              [".",".",".","4","1","9",".",".","5"],
#                              [".",".",".",".","8",".",".","7","9"]]))
# print(s.countAndSay("1"))
# print(s.checkString(s = "aaabbb"))
print(s.numberOfBeams(bank = ["000","111","000"]))


