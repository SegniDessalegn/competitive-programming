# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        changed = True
        while changed == True:
            changed = False
            curr = head
            prev = None
            while curr:
                if curr.val < x:
                    changed = True
                    if not prev:
                        head = curr.next
                    else:
                        prev.next = curr.next
                    curr.next = None
                    p.next = curr
                    p = p.next
                    break
                prev = curr
                curr = curr.next
        
        curr = head
        while curr:
            p.next = curr
            curr = curr.next
            p = p.next
        
        return dummy.next