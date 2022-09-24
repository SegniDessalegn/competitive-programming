# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = k
        temp = head
        while temp != None and n != 0:
            n -= 1
            temp = temp.next
        if n != 0:
            return head
        new_head, old_head, next_head = self.reverse(head, k)
        if next_head == None:
            return new_head
        old_head.next = self.reverseKGroup(next_head, k)
        return new_head

    def reverse(self, head, k):
        if head == None or head.next == None or k - 1 == 0:
            return head, head, head.next
        new_head, _, n = self.reverse(head.next, k - 1)
        head.next.next = head
        head.next = None
        return new_head, head, n
    