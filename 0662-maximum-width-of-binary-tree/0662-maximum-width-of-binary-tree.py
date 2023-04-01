# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        max_width = 1
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr[0].left:
                    queue.append((curr[0].left, 2 * curr[1]))
                if curr[0].right:
                    queue.append((curr[0].right, 2 * curr[1] + 1))
        
        return max_width