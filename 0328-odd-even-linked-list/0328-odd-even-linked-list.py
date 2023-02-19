# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            curr.next_node = curr.next.next
            curr = curr.next
        if curr:
            curr.next_node = None
        curr = head
        even_head = None
        if curr and curr.next:
            even_head = curr.next
        odd_tail = None
        counter = 0
        while curr:
            counter += 1
            if counter % 2 != 0:
                odd_tail = curr
            temp = curr.next
            curr.next = curr.next_node
            curr = temp
        if odd_tail:
            odd_tail.next = even_head
        return head