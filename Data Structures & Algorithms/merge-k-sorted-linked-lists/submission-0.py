# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(x, y):
    cpy = dummy = ListNode(0)    
    while x and y:
        if x.val > y.val:
            dummy.next = y
            dummy = dummy.next
            y =y.next 
        else:
            dummy.next = x
            dummy = dummy.next
            x = x.next
     
    if x:
       dummy.next = x
    else:
       dummy.next = y
    return cpy.next 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        res = lists[0]
        for elem in range(1, len(lists)):
            res = merge(res, lists[elem])
        
        return res 
            
        