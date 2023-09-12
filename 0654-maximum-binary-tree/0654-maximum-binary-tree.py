# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recur(left, right):
            if left > right:
                return None
            
            max_index = left
            max_num = nums[left]
            for i in range(left, right + 1):
                if nums[i] > max_num:
                    max_num = nums[i]
                    max_index = i
            
            left = recur(left, max_index - 1)
            right = recur(max_index + 1, right)
            
            curr = TreeNode(nums[max_index], left, right)
            
            return curr
        
        return recur(0, len(nums) - 1)