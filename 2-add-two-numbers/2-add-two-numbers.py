# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None
        units = (l1.val + l2.val) - (10 * ((l1.val + l2.val) // 10))
        tens = (l1.val + l2.val) // 10
        if l1.next == None and l2.next != None:
            l1.val = 0
            l2.next.val += tens
            return ListNode(units, self.addTwoNumbers(l1, l2.next))
        elif l2.next == None and l1.next != None:
            l2.val = 0
            l1.next.val += tens
            return ListNode(units, self.addTwoNumbers(l1.next, l2))
        elif l1.next == None and l2.next == None and tens != 0:
            return ListNode(units, ListNode(tens))
        elif l1.next != None:
            l1.next.val += tens
        elif l2.next != None:
            l2.next.val += tens
        return ListNode(units, self.addTwoNumbers(l1.next, l2.next))