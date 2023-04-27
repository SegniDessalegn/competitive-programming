# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = deque([root])
        ans = []
        while level:
            level_len = len(level)
            level_sum = 0
            for i in range(level_len):
                node = level.popleft()
                level_sum += node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ans.append(level_sum / level_len)
        
        return ans