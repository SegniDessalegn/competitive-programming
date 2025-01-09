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
        node_map = {}
        new_head = Node(-1, head)
        new_ptr = new_head
        ptr = head
        while ptr:
            new_node = Node(ptr.val)
            node_map[ptr] = new_node
            new_ptr.next = new_node
            new_ptr = new_ptr.next
            ptr = ptr.next
        
        ptr = head
        new_ptr = new_head.next
        while ptr:
            if ptr.random:
                new_ptr.random = node_map[ptr.random]
            ptr = ptr.next
            new_ptr = new_ptr.next

        return new_head.next
