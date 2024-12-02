# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        ans = False
        def get_ans(root):
            nonlocal ans
            
            if not root:
                return -1
            if root.val == x or root.val == y:
                return 0
            
            left = get_ans(root.left)
            right = get_ans(root.right)
            
            if left > 0 and right > 0 and left == right:
                ans = True
            
            if left != -1:
                return 1 + left
            if right != -1:
                return 1 + right
            
            return -1
        
        get_ans(root)
        return ans
    