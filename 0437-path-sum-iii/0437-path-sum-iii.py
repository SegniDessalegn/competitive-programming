# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def traverse(root, curr_sum, pref):
            nonlocal count
            
            if not root:
                return
            
            curr_sum += root.val
            if curr_sum - targetSum in pref:
                count += pref[curr_sum - targetSum]
            pref[curr_sum] = pref.get(curr_sum, 0) + 1
            
            traverse(root.left, curr_sum, pref)
            traverse(root.right, curr_sum, pref)
            
            pref[curr_sum] -= 1
            curr_sum -= root.val
        
        count = 0
        traverse(root, 0, {0:1})
        return count