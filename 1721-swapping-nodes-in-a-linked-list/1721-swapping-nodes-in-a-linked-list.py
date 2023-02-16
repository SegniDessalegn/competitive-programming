# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    first = None
    second = None
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        self.helper(dummy, k)
        
        self.first.next, self.second.next = self.second.next, self.first.next
        self.first.next.next, self.second.next.next = self.second.next.next, self.first.next.next
        
        return dummy.next
    
    def helper(self, head, k, forward_count = 0):
        if not head:
            return 0
        
        if forward_count == k - 1:
            self.first = head
        forward_count += 1
        
        backward_count = self.helper(head.next, k, forward_count)
        if backward_count == k:
            self.second = head
        backward_count += 1
        
        return backward_count
        