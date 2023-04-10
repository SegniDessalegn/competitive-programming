# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, curr_ans = ""):
            nonlocal nums
            if not root.left and not root.right:
                curr_ans += str(root.val)
                nums.append(int(curr_ans))
                return
            if root.left:
                traverse(root.left, curr_ans + str(root.val))
            if root.right:
                traverse(root.right, curr_ans + str(root.val))
        
        nums = []
        traverse(root)
        return sum(nums)