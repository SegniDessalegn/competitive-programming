# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        if root is None:
            return None
        
        right = self.flatten(root.right)
        left = self.flatten(root.left)
        
        if left is None:
            return root
        
        curr = left
        while curr and curr.right is not None:
            curr = curr.right
        
        if curr:
            curr.right = right
        
        root.right = left
        root.left = None
        
        return root
        