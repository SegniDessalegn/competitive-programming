class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_map = {0:1}
        cnt = 0
        ans = 0
        for i, n in enumerate(nums):
            if n % 2 != 0:
                cnt += 1
            if cnt - k in count_map:
                ans += count_map[cnt - k]
            if cnt not in count_map:
                count_map[cnt] = 0
            count_map[cnt] += 1
        return ans