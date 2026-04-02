"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        mapper = {None: None}
        while curr:
            copynode = Node(curr.val)
            mapper[curr] = copynode
            curr = curr.next
        
        curr = head
        while curr:
            mapper[curr].next = mapper[curr.next]
            mapper[curr].random = mapper[curr.random]
            curr = curr.next

        return mapper[head]



        