class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        cumulative_sum = [0]
        for i in nums:
            cumulative_sum.append(cumulative_sum[-1] + i)
        ans = len(nums) + 1
        monoq = deque()
        for index, sum in enumerate(cumulative_sum):
            while monoq and sum <= cumulative_sum[monoq[-1]]:
                monoq.pop()
            while monoq and sum - cumulative_sum[monoq[0]] >= k:
                ans = min(ans, index - monoq.popleft())
            monoq.append(index)
        return ans if ans < len(nums) + 1 else -1
    