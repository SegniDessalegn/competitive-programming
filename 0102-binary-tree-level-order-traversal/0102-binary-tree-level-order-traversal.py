class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([(root, 1)])
        ans = {}
        while queue:
            curr, level = queue.popleft()
            if level not in ans: ans[level] = []
            ans[level].append(curr.val)
            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
        return ans.values()
