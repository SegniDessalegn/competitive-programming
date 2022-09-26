# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head.next.next
        head.next.next = head
        head = head.next
        head.next.next = temp
        head.next.next = self.swapPairs(head.next.next)
        return head