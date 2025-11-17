# Pacific Atlantic Water Flow
# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

# Example 1:
# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]

# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]


# Example 2:

# Input: heights = [[1],[1]]

# Output: [[0,0],[0,1]]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0]) 
        can_reach_pacific,can_reach_atlantic = set(),set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        # make two sets for pacific and atlantic reachable cells
        # dfs from ocean sides and mark all reachable cells (height now can only go up from previouse height)
        # then find intersection of two sets and that is all cells that can reach both oceans
        def dfs(r,c, visited,prevHeight):
            if ((r,c) in visited or r<0 or c<0 or r==rows or c==cols or heights[r][c]<prevHeight):
                return
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                dfs(nr,nc,visited,heights[r][c])


        for c in range(cols):
            dfs(0,c,can_reach_pacific,heights[0][c])
            dfs(rows-1,c,can_reach_atlantic,heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,can_reach_pacific,heights[r][0])
            dfs(r,cols-1,can_reach_atlantic,heights[r][cols-1])

        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in can_reach_atlantic and (r,c) in can_reach_pacific:
                    res.append([r,c])
        return res