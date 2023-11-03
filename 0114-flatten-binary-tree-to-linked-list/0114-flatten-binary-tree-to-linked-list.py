# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        if root is None:
            return None, None
        
        right, right_ptr = self.flatten(root.right)
        left, left_ptr = self.flatten(root.left)
        
        if left_ptr is None and right_ptr is None:
            return root, root
        elif left_ptr is None and right_ptr is not None:
            return root, right_ptr
        elif right_ptr is None and left_ptr is not None:
            root.right = left
            root.left = None
            return root, left_ptr
        else:
            left_ptr.right = right
            root.right = left
            root.left = None
            return root, right_ptr
