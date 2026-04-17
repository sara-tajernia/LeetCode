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


    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for w in asteroids:
            if mass < w:
                return False
            mass += w 
        return True

    # def minOperations(self, nums, x):
    #     target = sum(nums) - x
    
    #     if target < 0:
    #         return -1
    #     if target == 0:
    #         return len(nums)
        
    #     print(target)
    #     left = 0
    #     max_length = -1
    #     current_sum = 0

    #     for i in range(len(nums)):
    #         if current_sum+nums[i] < target:
    #             max_length += 1
    #             current_sum += nums[i]

    #         elif current_sum+nums[i] > target:
                

    # def incremovableSubarrayCount(self, nums):
    #     n = len(nums)

    #     # Step 1: longest increasing prefix
    #     left = 0
    #     while left + 1 < n and nums[left] < nums[left + 1]:
    #         left += 1

    #     # If already strictly increasing
    #     if left == n - 1:
    #         return n * (n + 1) // 2

    #     ans = left + 2  # remove suffixes

    #     # Step 2: process suffix
    #     right = n - 1
    #     while right > 0:
    #         # ensure suffix is increasing
    #         if right < n - 1 and nums[right] >= nums[right + 1]:
    #             break

    #         # move left pointer to satisfy bridge condition
    #         while left >= 0 and nums[left] >= nums[right]:
    #             left -= 1

    #         ans += left + 2
    #         right -= 1

    #     return ans

    def numberGame(self, nums):
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
    
    def maximizeSquareArea(self, m, n, hFences, vFences):
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]

        hset = set()
        vset = set()
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                hset.add(abs(hFences[j] - hFences[i]))

        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                vset.add(abs(vFences[j] - vFences[i]))

        common = hset & vset
        if not common:
            return -1

        side = max(common)
        MOD = 10**9 + 7
        return (side * side) % MOD
    
    def hasTrailingZeros(self, nums):
        count = 0
        for n in nums:
            if n%2 == 0:
                count += 1
                if count == 2:
                    return True
                
        return False
    
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        
        pass_set = set(passengers)
        
        i = 0  
        n = len(passengers)
        
        for b in buses:
            cnt = 0
            
            while i < n and passengers[i] <= b and cnt < capacity:
                last = passengers[i]
                i += 1
                cnt += 1
            
            if cnt < capacity:
                last = b
        
        res = last
        while res in pass_set:
            res -= 1
        
        return res


    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        heapq = [-x for x in diffs]
        heapq.heapify(heapq)
        k = k1 + k2

        while k > 0 and diffs[0] > 0:
            # dont use _heappop_max
            heapq = [-x for x in diffs]
            heapq.heapify(heapq)
            max_diff = -heapq.heappop(heapq)
            max_diff -= 1
            heapq.heappush(heapq, -max_diff)
            diffs = [-x for x in heapq]
            k -= 1

        return sum(diff ** 2 for diff in diffs)
    

    def fillCups(self, A):
        return max(max(A), (sum(A) + 1) // 2)
                

    def canChange(self, start, target):
        if len(start) != len(target):
            return False
        if start.replace("_", "") != target.replace("_", ""):
            return False
        isLeft, isRight = False, False
        for s, t in zip(start, target):
            print(s, t)
            if not isRight and s == "R":
                isRight = True
            elif isRight and s =="R":
                isLeft = False
            elif not isRight and t=="R":
                return False

            if not isLeft and t == "L":
                isLeft = True
                print("sdfdsf", isLeft)
            elif isLeft and s =="L":
                isLeft = False
                print("isLeft", isLeft)
            elif not isLeft and s =="L":
                return False
        return True
        
    def totalMoney(self, n):
        if n == 0:
            return 0
        
        last_monday = 1
        last_day = 1
        total = 1
        for i in range(2, n+1):
            if i%7 == 1:
                last_monday += 1
                total += last_monday
                last_day = last_monday
            else:
                last_day += 1
                total += last_day

        return total
        

    # def maximumGain(self, s, x, y):
    #     if x < y:
    #         prior = "ba"
    #         second = "ab"
    #     else:
    #         prior = "ab"
    #         second = "ba"
    #     print(prior, second)
    

    #     total = 0
    #     while True:
    #         while prior in s:
    #             s = s.replace(prior, "", 1)
    #             total += max(x,y) 
    #         if second in s:
    #             s = s.replace(second, "", 1)
    #             total += min(x,y)
    #             continue
    #         else:
    #             return total

            
    # def constructDistancedSequence(self, n):
    #     res = [-1] * (2*n - 1)
    #     print(res)
    #     for i in range(n, 0,-1):
    #         print(i)
    #         for j in range(len(res)):
    #             print(j, j+i, "fggsd")
    #             if i == 1 and res[j]==-1:
    #                 res[j] = 1
    #                 break

    #             if res[j] == -1 and res[j+i] == -1:
    #                 res[j] = i
    #                 res[j+i] = i
    #                 # print(res[j], res[j+i])
    #                 print(res)
    #                 break
    #     return res
                
    # def constructDistancedSequence(self, n):
    #     res = [-1] * (2 * n - 1)
    #     used = [False] * (n + 1)

    #     def backtrack(pos):
    #         # If we filled the whole array → done
    #         if pos == len(res):
    #             return True

    #         # Skip already filled positions
    #         if res[pos] != -1:
    #             return backtrack(pos + 1)

    #         # Try numbers from large → small (greedy for lexicographically largest)
    #         for num in range(n, 0, -1):
    #             if used[num]:
    #                 continue

    #             if num == 1:
    #                 # Place 1 only once
    #                 res[pos] = 1
    #                 used[1] = True

    #                 if backtrack(pos + 1):
    #                     return True

    #                 # 🔙 backtrack
    #                 res[pos] = -1
    #                 used[1] = False

    #             else:
    #                 # Check bounds + availability
    #                 if pos + num < len(res) and res[pos] == -1 and res[pos + num] == -1:
    #                     res[pos] = res[pos + num] = num
    #                     used[num] = True

    #                     if backtrack(pos + 1):
    #                         return True

    #                     # 🔙 backtrack
    #                     res[pos] = res[pos + num] = -1
    #                     used[num] = False

    #         return False

    #     backtrack(0)
    #     return res

    def sequence_variant(self, n):
        seq = [0] * (2 * n - 1)  # matches your example size
        
        stack = [(n, seq[:])]
        
        while stack:
            k, curr = stack.pop()
            
            if k == 0:
                return curr
            
            for i in range(len(curr) - k):
                if curr[i] == 0 and curr[i + k] == 0:
                    new_seq = curr[:]
                    new_seq[i] = k
                    new_seq[i + k] = k
                    
                    stack.append((k - 1, new_seq))
        
        return None
                    
        

# class SmallestInfiniteSet(object):

#     def __init__(self):
        

#     def popSmallest(self):
#         """
#         :rtype: int
#         """
        

#     def addBack(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
        


        


        
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
# print(s.numberOfBeams(bank = ["000","111","000"]))
# print(s.asteroidsDestroyed(mass = 5, asteroids = [4,9,23,4]))
# print(s.minOperations(nums = [3,2,20,1,1,3], x = 10))
# print(s.incremovableSubarrayCount([8,7,6,6]))
# print(s.numberGame(nums = [2,5]))
# print(s.maximizeSquareArea(m = 3, n = 9, hFences = [2], vFences = [8,6,5,4]))
# print(s.hasTrailingZeros(nums = [1,3,5,7,9])) 
# print(s.latestTimeCatchTheBus(buses = [3], passengers = [2,4], capacity = 2))
# print(s.latestTimeCatchTheBus(buses = [10,20], passengers = [2,17,18,19], capacity = 2))
# print(s.latestTimeCatchTheBus(buses = [3], passengers = [2], capacity = 2))
# print(s.latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2))
# print(s.minSumSquareDiff(nums1 = [7,5,0,12,14], nums2 = [7,5,0,12,14], k1 = 2, k2 = 9))
# print(s.fillCups(amount = [5,4,4]))
# print(s.canChange(start = "_LL__R__R_", target = "L___L___RR"))
# print(s.totalMoney(n = 20))
# print(s.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))
print(s.sequence_variant(n = 13))


