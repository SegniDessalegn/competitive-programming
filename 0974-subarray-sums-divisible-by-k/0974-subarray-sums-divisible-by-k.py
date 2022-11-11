class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_map = {0:1}
        pre_sum = 0
        ans = 0
        for n in nums:
            pre_sum += n
            if pre_sum % k in sum_map:
                ans += sum_map[pre_sum % k]
            sum_map[pre_sum % k] = sum_map.get(pre_sum % k, 0) + 1
        return ans