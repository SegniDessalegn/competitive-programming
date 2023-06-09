# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr_head = dummy
        while curr_head:
            curr = curr_head.next
            s = 0
            no_zero = True
            while curr:
                s += curr.val
                if s == 0:
                    curr_head.next = curr.next
                    no_zero = False
                    break
                curr = curr.next
            if no_zero:
                curr_head = curr_head.next
        
        return dummy.next