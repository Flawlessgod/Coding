# Surrounded Regions
# You are given a 2-D matrix board containing 'X' and 'O' characters.

# If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

# Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

# Example 1:



# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","O","O","X"],
#   ["X","X","X","O"]
# ]

# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","O"]
# ]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if (r<0 or c<0 or c>=cols or r>=rows or board[r][c]!="O"):
                return
            board[r][c] = "T"
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                dfs(r,c)
        
        # 1 capture unsurrounded regrions and convert to temprorary variable
        # unsurrounded are by definition connected to edge of grid either directely or through adjacency 
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r in [0,rows-1] or c in [0,cols-1]):
                    dfs(r,c)


        # 2 convert surrounded region (o->x)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c]="X"
        # 3 unconvert t->o
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c]="O"