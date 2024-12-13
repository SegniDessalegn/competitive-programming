# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        result = 0
        
        def traverse(root):
            nonlocal result
            
            if not root:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)
            
            result += abs(left - right)
            
            return root.val + left + right
        
        traverse(root)
        return result