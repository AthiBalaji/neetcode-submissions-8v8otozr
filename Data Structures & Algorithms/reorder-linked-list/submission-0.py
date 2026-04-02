# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        #odd number case
        cpy = slow
        secondbeg = cpy.next
        # if fast:
        #     slow = slow.next
        cpy.next = None
        #reversing
        y = second = secondbeg
        prev = None
        while second:
            temp = second.next
            second.next = prev 
            prev = second
            second = temp 
        y = prev
        #iteration
        x = head
        while y:
            temp1 = x.next
            temp2 = y.next
            x.next = y 
            y.next = temp1 
            x = temp1
            y = temp2 






            
        