# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        all_nodes = []
        def dfs(node):
            if not node:
                return None
            nonlocal all_nodes
            all_nodes.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return None
        dfs(root)
        all_nodes.sort()
        return all_nodes[k-1]

        