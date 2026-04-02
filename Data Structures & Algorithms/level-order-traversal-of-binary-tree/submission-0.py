# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        bfs = deque()
        bfs.append(root)
        if not root:
            return []
        while bfs:
            nodes = []
            for i in range(len(bfs)):
                node = bfs.popleft()
                nodes.append(node)
            node_values = []
            for node in nodes:
                node_values.append(node.val)

                if node.left:
                    bfs.append(node.left)

                if node.right:
                    bfs.append(node.right)
            res.append(node_values)
        return res 
        