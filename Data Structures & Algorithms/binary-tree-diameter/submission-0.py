# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            self.res = 0
            def dfs(curr: Optional[TreeNode]) -> int:
                if not curr:
                    return 0
                l = dfs(curr.left)
                r = dfs(curr.right)
                h = max(1+l, 1+r)
                self.res = max(self.res, l+r)
                return h 
            dfs(root)
            return self.res
        