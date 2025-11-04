# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

# Example 1:



# Input: root = [1,2,3]
#   1
#  / \
# 2   3

# Output: [1,3]
# Example 2:



# Input: root = [1,2,3,4,5,6,7]
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7


# Output: [1,3,7]
# Constraints:

# 0 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100


# Problem Solution BFS

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft() # final iteration on bfs node will hold right side value
                if node:
                    rightSide = node    # set 
                    q.append(node.left)
                    q.append(node.right)
            if rightSide: 
                res.append(rightSide.val)

        return res