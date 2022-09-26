# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        node = head
        n = 0
        while node:
            stack.append(node.val)
            n += 1
            node = node.next
        largest = head.val
        i = 0
        while i <= (n / 2) - 1:
            twin_sum = stack[i] + stack[n - 1 - i]
            if twin_sum > largest:
                largest = twin_sum
            i += 1
        return largest