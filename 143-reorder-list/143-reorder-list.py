# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        deque = Deque()
        node = head
        while node:
            deque.append(node)
            node = node.next
            deque[-1].next = None
        head = deque.popleft()
        curr = head
        while deque:
            curr.next = deque.pop()
            curr = curr.next
            if deque:
                curr.next = deque.popleft()
            curr = curr.next
        return head