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
    def connect(self, root: 'Node') -> 'Node':
        # level order traversal using BFS
        # finish one level, do some operations on the level, pass to the next level
        
        if root is None:
            return root
        
        level = deque([root])
        while level:
            level_len = len(level)
            for i in range(level_len):
                node = level.popleft()
                if i < level_len - 1:
                    node.next = level[0]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        
        return root