"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        new_head = Node(x = head.val)
        curr = head.next
        new_head_curr = new_head
        while curr:
            new_head_curr.next = Node(x = curr.val)
            curr = curr.next
            new_head_curr = new_head_curr.next
        
        curr = head
        new_head_curr = new_head
        while curr:
            runner = head
            copy_runner = new_head
            while runner and runner is not curr.random:
                runner = runner.next
                copy_runner = copy_runner.next
            
            new_head_curr.random = copy_runner
            curr = curr.next
            new_head_curr = new_head_curr.next
        
        return new_head