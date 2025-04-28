from collections import Counter
from collections import deque, defaultdict
import math
import bisect
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
    
    def isValidSudoku(self, board):
        N = M = len(board)
        row_set = [set() for _ in range(N)]
        print(row_set)
        rows = defaultdict(list)
        cols = defaultdict(list)
        sqrs = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if (board[i][j] not in rows[i] and 
                        board[i][j] not in cols[j] and 
                        board[i][j] not in sqrs[3 * (j // 3) + (i // 3 + 1)]
                        ):
                        rows[i].append(board[i][j])
                        cols[j].append(board[i][j])
                        sqrs[3*(j//3) + (i//3 +1)].append(board[i][j])
                    else:
                        return False
                    
        return True
    

    # def divide(self, dividend, divisor):
        # sign = (dividend < 0) == (divisor < 0)
        # divisor = abs(divisor)
        # num = abs(dividend)
        # if divisor == 1 or divisor == -1:
        #     num = num if sign else -num
        #     if num < -2**31:
        #         return -2**31
        #     elif 2**31 -1 <num:
        #         return 2**31-1
        #     return num
        # counter = 0
        # while divisor <= num:
        #     num -= divisor
        #     counter += 1
        
        # counter = counter if sign else -counter
        # if counter < -2**31:
        #     return -2**31
        # elif 2**31 -1 <counter:
        #     return 2**31-1
        # return counter

    def myPow(self, x, n):
        results = {1: x}
        if n < 0:
            x = 1/x
            n = -n
        elif n == 0:
            return 1
        answer = x
        power = 1
        while power < n:
            if power < n/2:
                answer = answer * answer
                power += power
            else:
                answer *= x
                power += 1
        return answer
    
    def convertToTitle(self, columnNumber):
        outside = columnNumber
        letters = []
        while columnNumber > 26:
            outside = columnNumber//26
            remain = columnNumber % 26
            if remain == 0:
                remain = 26
                outside -= 1
            letters.append(chr(64 + remain))
            columnNumber = outside

        letters.append(chr(64 + outside))
            
        return ''.join(letters[::-1])
    
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                # if i <=j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix

    def numOfSubarrays(self, arr):
        counter = 0
        for i in range(len(arr)):
            sub = []
            sum_sub = 0
            for j in range(i, len(arr)):
                sub.append(arr[j])
                sum_sub += arr[j]
                if sum_sub % 2 == 1:
                    counter += 1  
                if sum_sub == 0:
                    return 0              
        return counter
    
    def permute(self, nums):
        result = []

        def backtrack(path, remain):
            if not remain:
                result.append(path)
                return
            for i in range(len(remain)):
                backtrack(path + [remain[i]], remain[:i] + remain[i+1:])
            
        backtrack([], nums)
        return result
    
    def isHappy(self, n):
        checked = []
        while n != 1:
            value = 0
            digits = [int(digit) for digit in str(n)]
            for digit in digits:
                value += digit*digit
            if value not in checked:
                checked.append(value)
                n = value
            else:
                return False
        return True

    
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(path, target, start):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(path + [candidates[i]], target - candidates[i], i)

        backtrack([], target, 0)
        return result

    # def search(self, nums, target):
    #     if len(nums) == 1:
    #         if nums[0] == target:
    #             return 0
    #         else:
    #             return -1
            
    #     left = 0
    #     right = len(nums)-1
    #     mid = int((right-left)/2) + left

    #     while left+1 != right:
    #         mid = int((right-left)/2) + left
    #         if nums[mid] < nums[left]:
    #             right = mid
    #         elif nums[right] < nums[mid]:
    #             left = mid 

    #     print(left, mid, right)
    #     if target <= nums[len(nums) -1]:
    #         search = nums[right:]
    #         print('111111111')
    #         counter = right
    #     else:
    #         search = nums[:right]
    #         print('22222222')
    #         counter = 0

    #     print(left, search)



    #     start = 0
    #     end = len(search) -1
    #     if target == search[start]:
    #         print('first')
    #         return counter
    #     if target == search[-1]:
    #         print('second')

    #         return len(search) -1 + counter 
        
    #     print(search)

    #     while start <= end:
    #         midel = int((end - start) / 2) + start
    #         print(search)
    #         if search[midel] == target:
    #             print('hiiiii',counter,  midel)
    #             return counter + midel
    #         elif search[midel] < search[start]:
    #             print(1, start, midel, end)
    #             end = midel - 1
    #         elif search[end] < search[midel]:
    #             start = midel + 1
    #             print(2, start, midel, end)
    #         else:
    #             if target < search[midel]:
    #                 end = midel - 1
    #             else:
    #                 start = midel + 1

    #         print(start, midel, end, '\n')
    #     print(987654, search)
    #     return -1  

    def mostProfitablePath(self, edges, bob, amount):
        print(edges)
        return
    
    def BFS(self, start, edges, amount):
        # Create a graph from the edge list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Asvalueing it's an undirected graph
        print(graph)
        
        # BFS setup
        queue = deque([start])
        visited = set([start])
        max_amount = amount[start]  # Initialize max_amount with the start node's amount

        # BFS loop
        while queue:
            current = queue.popleft()
            # Update the maximum amount found so far
            max_amount = max(max_amount, amount[current])
            
            # Visit all adjacent nodes
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print(max_amount)
        return max_amount
    

    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            sorted_letters = tuple(sorted(word))
            if sorted_letters in groups:
                groups[sorted_letters].append(word)
            else:
                groups[sorted_letters] = [word]

        return list(groups.values())
    
    def countAndSay(self, n):
        if n == 1:
            return '1'

        num = ['1', '1']
        for i in range(n-2):
            changed = []
            counter = 1
            for i in range(len(num)):
                if i != len(num) -1:
                    if num[i] == num[i+1]:
                        counter += 1
                    else:
                        changed.append(str(counter))
                        changed.append(num[i])
                        counter = 1
                else:
                    # print('auhdsfcaz',changed)
                    changed.append(str(counter))
                    changed.append(num[i])
                    counter = 1

            num = changed
        return ''.join(num)
    
    def majorityElement(self, nums):
        majority = {}
        for n in nums:
            if n in majority:
                majority[n] += 1
            else:
                majority[n] = 1

        return max(majority, key=majority.get)


    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    
    def isIsomorphic(self, s, t):
        isomorphic = {}
        s = list(s)
        t = list(t)
        if len(s) != len(t):
            return False
            
        for char in range(len(s)):
            # print(isomorphic.values)
            if s[char] not in isomorphic:
                if t[char] not in isomorphic.values():
                    isomorphic[s[char]] = t[char]
                else:
                    return False
            else:
                if isomorphic[s[char]] != t[char]:
                    return False
        return True

    def jump(self, nums):
        if len(nums) == 1:
            return 0
        
        jumps = 0
        position = 0
        position_value = nums[0]
    
        while position + position_value + 1 < len(nums):
            max_value = 0
            max_index = 0
            for i in range(position+1,  position + position_value + 1):
                if max_value <= nums[i] + i:
                    max_value = nums[i] + i
                    max_index = i
            
            jumps += 1

            position = max_index
            position_value = nums[position]

        return jumps + 1

    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  


        longest = ""
        for i in range(len(s)):
            odd = expandAroundCenter(i, i)
            even = expandAroundCenter(i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest
    
    def uniquePaths(self, m, n):
        return math.factorial(n+m-2) // (math.factorial(n-1) * math.factorial(m-1))
    
    def missingNumber(self, nums):
        result = [-1] * (len(nums)+1)
        for n in nums:
            result[n] = n
        for i in range(len(result)):
            if result[i] == -1:
                return i 
            
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            print(123456, nums[i])
            if nums[i] == 0:
                nums.pop(i)
                print('removed', nums)
                nums.append(0)
                print('added', nums)
        return nums

    def canWinNim(self, n):
        return False if n % 4 == 0 else True
    
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)):
            for j in range(i+1, i+k+1):
                if j < len(nums):
                    print(nums[i], nums[j])
                    if nums[i] == nums[j]:
                        print('this', nums[i], nums[j])
                        return True
            
        return False
    
    def addDigits(self, num):
        while 9 < num:
            num =  num//10 + num%10
        return num
    
    def wordPattern(self, pattern, s):
        map1 = {}
        map2 = {}
        pattern = list(pattern)
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] in map1:
                if map1[pattern[i]] != s[i]:
                    return False
            else:
                map1[pattern[i]] = s[i]
            if s[i] in map2:
                if map2[s[i]] != pattern[i]:
                    return False
            else:
                map2[s[i]] = pattern[i]
        return True
    
    def isPowerOfThree(self, n):
        # x = n ** (1/3)
        # print(x)
        # return x ** 3 == n


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
    # print(Solution.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
    # print(Solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
    #                             ,["6",".",".","1","9","5",".",".","."]
    #                             ,[".","9","8",".",".",".",".","6","."]
    #                             ,["8",".",".",".","6",".",".",".","3"]
    #                             ,["4",".",".","8",".","3",".",".","1"]
    #                             ,["7",".",".",".","2",".",".",".","6"]
    #                             ,[".","6",".",".",".",".","2","8","."]
    #                             ,[".",".",".","4","1","9",".",".","5"]
    #                             ,[".",".",".",".","8",".",".","7","9"]]))
    # print(Solution.divide(dividend = -2147483648, divisor = 1))
    # print(Solution.myPow(x = 0.00001, n = 2147483647))
    # print(Solution.convertToTitle(columnNumber=702))
    # print(Solution.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
    # print(Solution.numOfSubarrays(arr=[1,2,3,4,5,6,7]))
    # print(Solution.permute(nums=[1,2,3]))
    # print(Solution.isHappy(n=2)) 
    # print(Solution.combinationSum(candidates = [2], target = 1))
    # print(Solution.search(nums = [1,3], target =1))
    # print(Solution.mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount= [-2,4,2,-4,6]))
    # print(Solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
    # print(Solution.countAndSay(n=0))
    # print(Solution.majorityElement(nums = [2,2,1,1,1,2,2]))
    # print(Solution.containsDuplicate(nums=[1,2,3,4,1])) 
    # print(Solution.isIsomorphic(s="badc", t = "baba"))
    # print(Solution.jump(nums = [2,3,1,1,4]))
    # print(Solution.longestPalindrome(s = "ksjdiabcdcbajskducbs"))
    # print(Solution.uniquePaths(m = 3, n = 7))
    # print(Solution.missingNumber(nums = [3, 0,1]))
    # print(Solution.moveZeroes(nums = [0,0,1]))
    # print(Solution.canWinNim(n = 1))
    # print(Solution.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
    # print(Solution.addDigits(num = 38))
    # print(Solution.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
    print(Solution.isPowerOfThree(n = 28))

