# You are given a m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is one of {-1, 0, 2147483647}


# problem Solution BFS on gates
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        q = deque()


        def addRoom(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or grid[r][c]== -1):
                return
            visited.add((r,c))
            q.append([r,c])


        # add all gates and do multi bfs on gates
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visited.add((r,c))

        

        distance = 0 # gates are set to zero
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance # set distance
                
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            
            distance+=1    # increment as you've taken a step from a gate
