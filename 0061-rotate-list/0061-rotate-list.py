# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        k = k % length
        
        prev_head = head
        curr = head
        prev = None
        counter = 0
        while curr:
            if counter == length - k:
                head = curr
                prev.next = None
            counter += 1
            prev = curr
            curr = curr.next
        
        if prev_head is not head:
            prev.next = prev_head
        
        return head