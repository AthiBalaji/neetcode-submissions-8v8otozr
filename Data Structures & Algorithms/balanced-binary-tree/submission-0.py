# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag =True
        def dfs(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0 
            l = dfs(curr.left)
            r = dfs(curr.right)
            if(abs(l-r))>1:
                self.flag = False
            h = 1+max(l,r)
            return h
        dfs(root)
        return self.flag

        