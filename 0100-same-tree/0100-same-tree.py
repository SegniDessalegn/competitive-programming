class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p is q
        
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            if curr1.val != curr2.val:
                return False
            
            if curr1.right:
                if not curr2.right:
                    return False
                stack1.append(curr1.right)
            if curr1.left:
                if not curr2.left:
                    return False
                stack1.append(curr1.left)
            
            if curr2.right:
                if not curr1.right:
                    return False
                stack2.append(curr2.right)
            if curr2.left:
                if not curr1.left:
                    return False
                stack2.append(curr2.left)
            
        return True