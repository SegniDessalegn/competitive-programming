# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def recur(root, curr):
            nonlocal ans
            if not root:
                return ""
            if root.left:
                recur(root.left, chr(root.val + 97) + curr)
            if root.right:
                recur(root.right, chr(root.val + 97) + curr)
            if not root.left and not root.right:
                if not ans:
                    ans = chr(root.val + 97) + curr
                else:
                    ans = min(ans, chr(root.val + 97) + curr)
        
        ans = None
        recur(root, "")
        
        return ans