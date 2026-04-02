"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        created = {}
        q = deque()
        created[node] = Node(node.val)
        q.append(node)

        while q:
            n = q.popleft()
            for nn in n.neighbors:
                if nn not in created:
                    created[nn] = Node(nn.val)
                    q.append(nn)  

                created[n].neighbors.append(created[nn])

        
        return created[node]

        


        