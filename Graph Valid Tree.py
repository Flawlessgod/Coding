# Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:
# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output:
# true

# Example 2:
# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output:
# false

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # definition of a graph is all nodes are connected and there is no loop present

        # no graphs given
        if not n:
            return True

        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        def dfs(i,prev):
            if i in visited:
                return False
            visited.add(i)

            for j in adj[i]:
                # dont go back to node you were just at
                if j == prev:
                    continue
                
                if not dfs(j,i):
                    return False
            return True

        # first prev value = -1 becuase -1 will never be in our list
        return dfs(0,-1) and n==len(visited)