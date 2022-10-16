class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0:1}
        prefix_sum = 0
        ans = 0
        for i in nums:
            prefix_sum += i
            ans += sum_map.get(prefix_sum - k, 0)
            sum_map[prefix_sum] = 1 + sum_map.get(prefix_sum, 0)
        return ans