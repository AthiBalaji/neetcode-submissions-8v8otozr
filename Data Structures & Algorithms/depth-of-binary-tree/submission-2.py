# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        bfs = deque()
        bfs.append(root)
        if not root:
            return 0 
        max_depth = 0
        while bfs:
            for i in range(len(bfs)):
                a = bfs.popleft()
                if a.left:
                    bfs.append(a.left)
                if a.right:
                    bfs.append(a.right)
            max_depth+=1          
        return max_depth
        
        