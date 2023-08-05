# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def backTrack(curr):
            if len(curr) == 0:
                return [None]
            if len(curr) == 1:
                return [TreeNode(val = curr[0])]
            
            curr = list(curr)
            trees = []
            for i in range(len(curr)):
                left = backTrack(tuple(curr[:i]))
                right = backTrack(tuple(curr[i + 1:]))
                
                for n1 in left:
                    for n2 in right:
                        head = TreeNode(val = curr[i], left = n1, right = n2)
                        trees.append(head)
            
            return trees
        
        return backTrack(tuple([i for i in range(1, n + 1)]))