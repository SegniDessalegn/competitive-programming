class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        ans = 0
        for i in range(N):
            ans += abs(nums1[i] - nums2[i])
        
        sorted_nums1 = sorted(nums1)
        real_ans = ans
        for i in range(N):
            idx = bisect_left(sorted_nums1, nums2[i])
            a1, a2, a3 = float("inf"), float("inf"), float("inf")
            if idx < N:
                a1 = ans - abs(nums1[i] - nums2[i]) + abs(sorted_nums1[idx] - nums2[i])
            if idx < N - 1:
                a2 = ans - abs(nums1[i] - nums2[i]) + abs(sorted_nums1[idx + 1] - nums2[i])
            if idx > 0:
                a3 = ans - abs(nums1[i] - nums2[i]) + abs(sorted_nums1[idx - 1] - nums2[i])
            
            real_ans = min(real_ans, min(a1, a2, a3))
            
        return real_ans % (10 ** 9 + 7)