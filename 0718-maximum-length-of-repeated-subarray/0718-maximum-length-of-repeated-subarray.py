class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        dp = {(i, j):0 for i in range(N1 + 1) for j in range(N2 + 1)}
        
        for i in range(N1 - 1, -1, -1):
            for j in range(N2 - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[(i, j)] = 1 + dp[(i + 1, j + 1)]
        
        return max(dp.values())