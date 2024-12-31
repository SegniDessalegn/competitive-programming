# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head):
            if not head or not head.next:
                return head
            new_head = reverse(head.next)
            head.next.next = head
            head.next = None
            return new_head
        
        head = ListNode(-1, head)
        prev = head
        curr = head.next
        count = 0
        while curr:
            count += 1
            if count == k:
                temp = curr.next
                curr.next = None
                
                temp2 = prev.next
                new_head = reverse(temp2)
                prev.next = new_head
                
                temp2.next = temp
                
                prev = temp2
                curr = temp
                count = 0
            else:
                curr = curr.next

        return head.next
    