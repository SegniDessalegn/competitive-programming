"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        result = head
        temps = []
        while head:
            if head.child:
                if head.next:
                    temps.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            
            if head.next is None and temps:
                curr = temps.pop()
                head.next = curr
                curr.prev = head
            
            head = head.next
        
        return result
    