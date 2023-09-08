# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        curr_level = deque([root])
        max_sum = root.val
        ans = 1
        level = 1
        while curr_level:
            length = len(curr_level)
            curr_sum = 0
            for _ in range(length):
                curr = curr_level.popleft()
                curr_sum += curr.val
                if curr.right:
                    curr_level.append(curr.right)
                if curr.left:
                    curr_level.append(curr.left)
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = level
            level += 1
        
        return ans