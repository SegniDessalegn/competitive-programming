# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        level = [root]
        is_even = True
        while level:
            next_level = []
            prev = None
            for i in range(len(level)):
                if (is_even and level[i].val % 2 == 0) or (not is_even and level[i].val % 2 != 0):
                    return False
                if prev is not None and ((is_even and level[i].val <= prev) or (not is_even and level[i].val >= prev)):
                    return False
                prev = level[i].val
                if level[i].left:
                    next_level.append(level[i].left)
                if level[i].right:
                    next_level.append(level[i].right)
            
            level = next_level[:]
            is_even = not is_even
        
        return True