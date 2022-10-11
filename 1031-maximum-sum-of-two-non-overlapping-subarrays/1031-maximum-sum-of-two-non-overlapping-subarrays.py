class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)
        max_sum, ans = 0, 0
        i = firstLen
        while i < len(prefix_sum) - secondLen:
            max_sum =  max(max_sum, prefix_sum[i] - prefix_sum[i - firstLen])
            ans = max(ans, max_sum + prefix_sum[i + secondLen] - prefix_sum[i])
            i += 1
        max_sum = 0
        i = secondLen
        while i < len(prefix_sum) - firstLen:
            max_sum =  max(max_sum, prefix_sum[i] - prefix_sum[i - secondLen])
            ans = max(ans, max_sum + prefix_sum[i + firstLen] - prefix_sum[i])
            i += 1
        return ans