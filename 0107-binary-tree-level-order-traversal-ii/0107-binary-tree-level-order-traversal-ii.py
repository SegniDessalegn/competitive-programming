# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level = deque([root])
        ans = []
        while level:
            level_len = len(level)
            ans.append([])
            for i in range(level_len):
                node = level.popleft()
                ans[-1].append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        
        return ans[::-1]