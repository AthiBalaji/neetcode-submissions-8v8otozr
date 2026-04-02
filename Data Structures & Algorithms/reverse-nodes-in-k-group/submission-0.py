# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total = 0
        curr = head
        while curr:
            curr = curr.next
            total+=1
        
        groups = total//k

        if groups == 0:
            return head 
        prev = None
        fi = None
        res = None
        curr = head
        while groups != 0:
            print("groups", groups)
            run =0 
            init = curr
            print("init", init.val)
            while run < k:
                print("run", run)
                temp = curr.next 
                curr.next = prev 
                prev = curr                 
                curr = temp 
 
                run+=1
            if fi:
                print("fi value and curr value",fi.val, prev.val)
                fi.next = prev
            else:
                res = prev
            fi = init 
            print("groups and fi ", groups, fi.val)
            groups -=1 
        
            fi.next = curr
        return res 
