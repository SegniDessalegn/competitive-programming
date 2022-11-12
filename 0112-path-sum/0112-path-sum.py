# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr_sum = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        self.curr_sum += root.val
        if not root.right and not root.left:
            is_equal = targetSum == self.curr_sum
            self.curr_sum -= root.val
            return is_equal
        is_equal = self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        self.curr_sum -= root.val
        return True if is_equal else False