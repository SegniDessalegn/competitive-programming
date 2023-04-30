# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path = self.path_containing(root, target)
        visited = set()
        ans = []
        for i in range(len(path)):
            ans.extend(self.get_nodes(path[i], k - i, visited))
            visited.add(path[i].val)
        return ans
    
    def path_containing(self, root, target):
        if not root:
            return []
        if root.val == target.val:
            return [root]
        left = self.path_containing(root.left, target)
        if left:
            left.append(root)
            return left
        right = self.path_containing(root.right, target)
        if right:
            right.append(root)
            return right
        
        return []
    
    def get_nodes(self, root, dist, visited = set()):
        if not root or root.val in visited:
            return []
        if dist == 0:
            return [root.val]
        ans = []
        ans.extend(self.get_nodes(root.left, dist - 1, visited))
        ans.extend(self.get_nodes(root.right, dist - 1, visited))
        return ans