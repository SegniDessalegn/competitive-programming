# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = self.count_nodes(root, {})
        modes = []
        max_count = max(count.values())
        for n in count:
            if count[n] == max_count:
                modes.append(n)
            
        return modes
    
    
    def count_nodes(self, root, count):
        if not root:
            return count
        count[root.val] = count.get(root.val, 0) + 1
        self.count_nodes(root.left, count)
        self.count_nodes(root.right, count)
        return count