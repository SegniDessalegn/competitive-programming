# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val = float("inf"), next = head)
        return self.get_greater(dummy).next
    
    
    def get_greater(self, head):
        if not head.next:
            return head
        prev = self.get_greater(head.next)
        if prev.val <= head.val:
            head.next = prev
            return head
        else:
            return prev
        