# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        def dfs(root, parent):
            nonlocal start_node
            if not root:
                return
            if root.val == start:
                start_node = root
            root.parent = parent
            dfs(root.left, root)
            dfs(root.right, root)
        
        start_node = None
        dfs(root, None)
        queue = deque([(start_node, 0)])
        visited = set([start_node.val])
        max_time = 0
        
        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)
            for neighbour in [node.left, node.right, node.parent]:
                if neighbour and neighbour.val not in visited:
                    queue.append((neighbour, time + 1))
                    visited.add(neighbour.val)
        
        return max_time