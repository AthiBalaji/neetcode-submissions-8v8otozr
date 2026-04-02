# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs = deque()
        bfs.append(root)
        res = []
        if not root:
            return res
        while bfs:
            nodes = []
            for i in range(len(bfs)):
                nodes.append(bfs.popleft())
            res.append(nodes[-1].val)
            
            for node in nodes:
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return res
            
        