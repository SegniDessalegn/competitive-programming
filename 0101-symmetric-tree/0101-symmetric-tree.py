class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return  self.traverse(root.left, root.right)

    def traverse(self, left, right):
        if not left and not right:
            return True
        if (not left and right or not right and left) or left.val != right.val:
            return False
        return self.traverse(left.left, right.right) and self.traverse(left.right, right.left)
