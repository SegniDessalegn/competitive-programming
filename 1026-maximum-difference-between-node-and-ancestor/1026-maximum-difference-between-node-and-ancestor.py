# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def get_ans(root):
            nonlocal ans
            
            if not root:
                return (float("inf"), -float("inf"))
            
            ln, lx = get_ans(root.left)
            rn, rx = get_ans(root.right)
            
            if root.left:
                ans = max(ans, abs(root.val - ln), abs(root.val - lx))
            if root.right:
                ans = max(ans, abs(root.val - rn), abs(root.val - rx))
            
            return (min(ln, rn, root.val), max(lx, rx, root.val))
        
        ans = 0
        get_ans(root)
        return ans
    