# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_count = defaultdict(int)
        def traverse(root):
            if not root:
                return 0
            child_sum = root.val + traverse(root.left) + traverse(root.right)
            sum_count[child_sum] += 1
            return child_sum
        
        traverse(root)
        
        ans = []
        most_freq = 0
        for s in sum_count:
            if sum_count[s] > most_freq:
                ans = [s]
                most_freq = sum_count[s]
            elif sum_count[s] == most_freq:
                ans.append(s)
        
        return ans