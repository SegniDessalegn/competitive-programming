# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leafs(root):
            if not root:
                return []
            
            curr = []
            if not root.left and not root.right:
                curr.append(root.val)
            
            left = get_leafs(root.left)
            right = get_leafs(root.right)
            
            return left + curr + right
        
        return get_leafs(root1) == get_leafs(root2)
    