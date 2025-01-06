# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def traverse(root, column, level):
            if not root:
                return
            columns[column].append((level, root.val))
            traverse(root.left, column - 1, level + 1)
            traverse(root.right, column + 1, level + 1)
        
        columns = defaultdict(list)
        traverse(root, 0, 0)
        
        ans = []
        for key in sorted(columns.keys()):
            columns[key].sort()
            ans.append([num[1] for num in columns[key]])
        
        return ans
    