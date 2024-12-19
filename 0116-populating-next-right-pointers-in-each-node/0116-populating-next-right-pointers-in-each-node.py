"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        level = [root]
        while level:
            next_level = []
            prev = None
            for i in range(len(level)):
                if prev:
                    prev.next = level[i]
                prev = level[i]
                
                if level[i].left:
                    next_level.append(level[i].left)
                if level[i].right:
                    next_level.append(level[i].right)
            if prev:
                prev.next = None
            level = next_level[:]
        
        return root
    