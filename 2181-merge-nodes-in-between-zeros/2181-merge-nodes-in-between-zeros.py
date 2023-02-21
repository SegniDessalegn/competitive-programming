# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        dummy = head
        p = dummy
        while curr:
            val_sum = 0
            while curr and curr.val != 0:
                val_sum += curr.val
                curr = curr.next
            p.next = ListNode(val = val_sum)
            p = p.next
            curr = curr.next
        
        return dummy.next