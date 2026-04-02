# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = dummy = ListNode(0, head)
        prev = ListNode(0, dummy)
        while n > 0:
            right = right.next
            n-=1
        while right:
            prev = prev.next
            left = left.next
            right = right.next 

        prev.next = left.next 
        return dummy.next

        



        