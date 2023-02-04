# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        count = 0
        prev = None
        middle = head
        curr = head
        while curr:
            if count % 2 !=0 :
                prev = middle
                middle = middle.next
            curr = curr.next
            count += 1
        
        if prev is not None:
            prev.next = middle.next
        
        return head