# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            nonlocal ans
            if not root:
                return 0
            
            total_sum = root.val
            
            left_sum = helper(root.left)
            right_sum = helper(root.right)
            
            if left_sum > 0:
                total_sum += left_sum
            if right_sum > 0:
                total_sum += right_sum
            
            ans = max(ans, total_sum)
            
            return max(root.val, root.val + left_sum, root.val + right_sum)
        
        ans = -float("inf")
        helper(root)
        return ans