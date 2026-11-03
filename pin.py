def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def dfs(r, c):
        # Stop if outside the grid or water
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == "0"):
            return

        # Mark as visited
        grid[r][c] = "0"

        # Explore four directions
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right

    # Visit every cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)

    return islands


def find_clusters(near_dups):
    graph = {}
    for image, neighbors in near_dups.items():
        if image not in graph:
            graph[image] = set()
        for neighbor in neighbors:
            if neighbor not in graph:
                graph[neighbor] = set()
            graph[image].add(neighbor)
            graph[neighbor].add(image)

        # print(graph)

    visited = set()
    clusters = []

    def dfs(image, cluster):
        visited.add(image)
        cluster.append(image)
        for n in graph[image]:
            if n not in visited:
                dfs(n, cluster)


    for image, neighbors in graph.items():
        if image not in visited:
            cluster = []
            dfs(image, cluster)
            clusters.append(cluster)

            
        


    return clusters


near_dups = {
    "A": ["B", "I", "K"],
    "B": ["A", "D"],
    "C": ["E"],
    "D": [],
    "E": [],
    "F": [],
    "G": ["K"],
    "I": [],
    "K": []
}
# print(find_clusters(near_dups))




def celebrity(mat):
    if len(mat) == 1:
        return 0
    # visited = set()
    cellebs = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==1:
                # j is possible celeb
                if j not in cellebs:
                    cellebs[j] = [i]
                else:
                    cellebs[j].append(i)

    for key in cellebs:
        if len(cellebs[key]) == len(mat) :
            return 1 
    
    return -1



mat = [[1, 1, 0], 
        [0, 1, 0], 
        [0, 1, 1]]

# print(celebrity(mat))


import heapq

# 1. Define Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 2. Convert Python list into Linked List
def createLinkedList(values):
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# 3. Merge K Sorted Linked Lists
def mergeKLists(lists):
    min_heap = []

    # Add first node of each linked list
    for i, node in enumerate(lists):
        # print(f"Adding node with value {node.val} from list {i} to the heap")
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
    # print(f"Initial min_heap: {[(val, i) for val, i, _ in min_heap]}")  

    dummy = ListNode(0)
    current = dummy
    # print("Starting to merge lists...", current.val)


    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        print(f"Popped node with value {val} from list {i} from the heap")

        print(f"Adding node with value {node.val} to the merged list")
        current.next = node
        current = current.next

        # Add next node from the same list
        if node.next:
            heapq.heappush(
                min_heap,
                (node.next.val, i, node.next)
            )

    return dummy.next


# 4. Print Linked List
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# 5. Test
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

# linked_lists = [createLinkedList(lst) for lst in lists]

# result = mergeKLists(linked_lists)

# printList(result)




# class Solution(object):
def maxAreaOfIsland(grid):
    max_area = 0

    def dfs(i, j):
        if (i<0 or len(grid)<=i or
            j<0 or len(grid[0])<=j or
            grid[i][j] == 0):
            return 0

        area = 1
        grid[i][j] = 0
        area += dfs(i+1, j)
        area += dfs(i-1, j)
        area += dfs(i, j+1)
        area += dfs(i, j-1)

        return area



    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                area = dfs(i, j)
                max_area = max(max_area, area)

        
    return max_area


# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,1,1,0,1,0,0,0,0,0,0,0,0],
#         [0,1,0,0,1,1,0,0,1,0,1,0,0],
#         [0,1,0,0,1,1,0,0,1,1,1,0,0],
#         [0,0,0,0,0,0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid =[[0,0,0,0,0,0,0,0]]


# print(maxAreaOfIsland(grid))



from collections import deque

def orangesRotting(grid):

    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    fresh_count = 0
    munutes = -1
    visited = set()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i,j))
            elif grid[i][j] == 1:
                fresh_count += 1
    print(list(queue), len(queue))

    if len(queue) == 0:
        return -1 if 0<fresh_count else 0
    
    dirs = [(0,1), (1,0), (-1,0), (0,-1)]

    while 0 < len(queue):
    # while len(queue) < 4:
        cicle = len(queue)
        for n in range(cicle):
            i, j = queue.popleft()
            print(i, j, list(queue))

            for di, dj in dirs:
                r = di + i
                c = dj + j
                if 0<=r and r<rows and 0<=c and c<cols and grid[r][c] == 1:
                    if (r,c) not in queue:
                        queue.append((r,c))
                    grid[r][c] = 2
                    fresh_count -=1
        munutes += 1
        print('asdadds',list(queue), munutes)

    print (munutes, fresh_count)
    return munutes if fresh_count==0 else -1




grid = [[1]]

print(orangesRotting(grid))