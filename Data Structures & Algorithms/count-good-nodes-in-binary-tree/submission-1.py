# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(max_value, node):
            if not node:
                return 0
            if node.val >= max_value:
                max_value = max(max_value, node.val)
                return 1 + dfs(max_value,node.left) + dfs(max_value,node.right)
            else:
                max_value = max(max_value, node.val)
                return dfs(max_value, node.left) + dfs(max_value,node.right)
        count = dfs(root.val, root)
        return count
        