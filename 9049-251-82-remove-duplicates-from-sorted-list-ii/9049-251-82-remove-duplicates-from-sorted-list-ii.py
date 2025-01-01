# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        head = ListNode(None, head)
        valid = head
        prev = head.next
        curr = head.next.next
        duplicate = False
        while curr:
            if curr.val != prev.val:
                if duplicate:
                    valid.next = curr
                else:
                    valid = valid.next
                prev = curr
                duplicate = False
            else:
                duplicate = True
            curr = curr.next
        
        if duplicate:
            valid.next = None

        return head.next
    