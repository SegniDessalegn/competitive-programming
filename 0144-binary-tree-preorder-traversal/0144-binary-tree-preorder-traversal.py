# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        path = []
        while stack:
            curr = stack.pop()
            path.append(curr.val)
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)
        return path