# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next
        
        n = 0
        curr = list1
        a_node = list1
        b_node = list1
        while curr:
            if n == a - 1:
                a_node = curr
            if n == b + 1:
                b_node = curr
            curr = curr.next
            n += 1
        
        a_node.next = list2
        list2_tail.next = b_node
        
        return list1