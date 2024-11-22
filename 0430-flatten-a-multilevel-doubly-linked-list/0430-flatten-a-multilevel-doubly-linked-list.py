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
        
        def traverse(head):
            if not head:
                return None
            
            if not head.next:
                if head.child:
                    tail = traverse(head.child)
                    head.next = head.child
                    head.next.prev = head
                    head.child = None
                    return tail
                return head
            
            if head.child:
                tail = traverse(head.child)
                temp_next = head.next
                
                head.next = head.child
                head.next.prev = head
                head.child = None
                
                tail.next = temp_next
                tail.next.prev = tail
                
                return traverse(temp_next)
            else:
                return traverse(head.next)
        
        traverse(head)
        
        return head
    