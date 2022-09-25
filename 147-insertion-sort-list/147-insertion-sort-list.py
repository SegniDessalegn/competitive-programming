# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        empty = ListNode()
        empty.next = head
        curr = head
        prev = empty
        while curr:
            pos = empty
            inserted = False
            while pos != curr:
                if pos.next.val > curr.val:
                    insert = curr
                    prev.next = curr.next
                    curr = prev.next
                    insert.next = pos.next
                    pos.next = insert
                    inserted = True
                    break
                pos = pos.next
            if not inserted:
                curr = curr.next
                prev = prev.next
        return empty.next