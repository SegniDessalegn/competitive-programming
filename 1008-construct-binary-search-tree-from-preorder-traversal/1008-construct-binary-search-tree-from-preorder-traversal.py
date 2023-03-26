# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def construct(root):
            nonlocal i
            if not root or i == len(preorder):
                return
            if preorder[i] < preorder[i - 1]:
                root.left = TreeNode(preorder[i])
                i += 1
                construct(root.left)
        
        def getNext(root, curr):
            if not root:
                return None
            
            if curr < root.val:
                parent = getNext(root.left, curr)
                if not parent:
                    return root
                else:
                    return parent
            else:
                parent = getNext(root.right, curr)
                if not parent:
                    return root
                else:
                    return parent
        
        i = 1
        root = TreeNode(preorder[0])
        curr_root = root
        while i < len(preorder):
            construct(curr_root)
            if i >= len(preorder):
                break
            parent = getNext(root, preorder[i])
            parent.right = TreeNode(preorder[i])
            curr_root = parent.right
            i += 1
        
        return root