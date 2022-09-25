# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        mono_stack = []
        answer = []
        node = head
        index = 0
        while node:
            while mono_stack and mono_stack[-1][1] < node.val:
                answer[mono_stack.pop()[0]] = node.val
            answer.append(0)
            mono_stack.append((index, node.val))
            node = node.next
            index += 1
        return answer
    