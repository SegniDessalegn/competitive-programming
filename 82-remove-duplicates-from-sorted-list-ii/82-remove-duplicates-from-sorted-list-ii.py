# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        val = None
        curr = None
        while node:
            if not val and node.next and node.val == node.next.val:
                val = node.val
            elif not node.next or node.val != node.next.val:
                if val == None:
                    if curr == None:
                        head = node
                        curr = head
                    else:
                        curr.next = node
                        curr = curr.next
                else:
                    val = None
            node = node.next
            if curr != None:
                curr.next = None
            else:
                head = None
        return head