# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pos = {}
        def traverse(root, row = 0, col = 0):
            if not root:
                return
            if col not in pos:
                pos[col] = []
            pos[col].append((row, root.val))
            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)
        
        traverse(root)
        answer = []
        for n in sorted(pos.keys()):
            pos[n].sort()
            for i in range(len(pos[n])):
                pos[n][i] = pos[n][i][1]
            answer.append(pos[n])
        
        return answer