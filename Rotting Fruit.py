# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Example 1:
# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

# Output: 4
# Example 2:

# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

# Output: -1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 - empty
        # 1 - fresh
        # 2 - rotten

        # idea - from rotten fruits multisource bfs then relook at grid to see if there exists any fresh fruit

        rows,cols = len(grid),len(grid[0])
        q = deque()
        minutes,fresh = 0,0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1

                if grid[r][c] == 2: #make q of all inital rotten fruit locations
                    q.append([r,c])

        
        def addroom(r,c):
            nonlocal fresh
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!= 1):
                return
            grid[r][c]=2
            q.append([r,c])
            fresh-=1

        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=0
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
                

            minutes+=1
            

        return minutes if fresh==0 else -1