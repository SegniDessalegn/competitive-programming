# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        min_depth = 0
        queue = deque()
        queue.append(root)
        next_queue = deque()
        while queue:
            next_queue.clear()
            min_depth += 1
            while queue:
                curr = queue.popleft()
                if curr.right and curr.left:
                    next_queue.append(curr.right)
                    next_queue.append(curr.left)
                elif curr.right:
                    next_queue.append(curr.right)
                elif curr.left:
                    next_queue.append(curr.left)
                else:
                    return min_depth
            queue = next_queue.copy()
        return min_depth
