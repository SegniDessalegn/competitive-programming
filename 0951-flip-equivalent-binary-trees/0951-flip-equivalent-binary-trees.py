# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def flip(root1, root2):
            if not root1:
                return root2 is None
            if not root2:
                return root1 is None
            
            if root1.val != root2.val:
                return False
            
            return (flip(root1.left, root2.left) and flip(root1.right, root2.right)) or (flip(root1.left, root2.right) and flip(root1.right, root2.left))
            
        return flip(root1, root2)
    