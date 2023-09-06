# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_equality(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            # flip
            flip = get_equality(root1.left, root2.right) and get_equality(root1.right, root2.left)
            
            # not flip
            not_flip = get_equality(root1.left, root2.left) and get_equality(root1.right, root2.right)
            
            return flip or not_flip
        
        return get_equality(root1, root2)