# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.get_path(root, targetSum, 0, [], [])
    
    def get_path(self, root, targetSum, curr_sum, curr_path, ans):
        if not root:
            return ans
        curr_sum += root.val
        curr_path.append(root.val)
        if not root.right and not root.left:
            if curr_sum == targetSum:
                ans.append(curr_path.copy())
                curr_sum -= root.val
                curr_path.pop()
                return ans
        self.get_path(root.left, targetSum, curr_sum, curr_path, ans)
        self.get_path(root.right, targetSum, curr_sum, curr_path, ans)
        curr_sum -= root.val
        curr_path.pop()
        return ans