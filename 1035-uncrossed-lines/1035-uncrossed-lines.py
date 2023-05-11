class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        
        dp = {}
        
        def recur(i = -1, j = -1):
            if i >= l1 - 1 or j >= l2 - 1:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if nums1[i + 1] == nums2[j + 1]:
                dp[(i, j)] = 1 + recur(i + 1, j + 1)
            else:
                dp[(i, j)] = max(recur(i + 1, j), recur(i, j + 1))
            
            return dp[(i, j)]
        
        
        return recur()