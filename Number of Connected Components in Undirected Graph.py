# Number of Connected Components in an Undirected Graph
# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.

# Example 1:

# Input:
# n=3
# edges=[[0,1], [0,2]]

# Output:
# 1
# Example 2:

# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]

# Output:
# 2

from collections import deque
from typing import List 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False]*n
        
        #append edges to adjacency list
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
         
         #set all nodes in component to visited by iterating through ajacency list
        def bfs(node):
            q = deque([node])
            visited[node] = True

            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

        res = 0
        for node in range(n):
            if not visited[node]:
                bfs(node)
                res+=1
        return res 
    
n=3
edges=[[0,1],[0,2]]
print(Solution().countComponents(n,edges))

n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
print(Solution().countComponents(n,edges))