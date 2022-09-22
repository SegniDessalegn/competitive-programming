# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        node = head
        length = 0
        remove = head
        while node != None:
            length += 1
            node = node.next
            if length > n + 1:
                remove = remove.next
        if n == length:
            head = head.next
        remove.next = remove.next.next
        return head