# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
# Example 1:

# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1
# Example 2:

# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4
# Constraints:

# 1 <= grid.length, grid[i].length <= 100
# grid[i][j] is '0' or '1'.


# Problem Solution BFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        if not grid:
            return 0

        #queue for rows in bfs
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            # set current grid location to 0 and add adjacent 1's if present. 
            grid[r][c]="0"

            while q:
                row,col = q.popleft()
                #row,col = q.pop() # DFS approach


                for dr,dc in directions:
                    nr, nc = row+dr, col+dc
                    if ( nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0" ):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = "0"


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands

