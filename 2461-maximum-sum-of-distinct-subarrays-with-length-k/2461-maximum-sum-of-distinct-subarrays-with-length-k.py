class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = {}
        _sum = 0
        ans = 0
        j = 0
        for i in range(N):
            if i >= k:
                _sum -= nums[j]
                count[nums[j]] -= 1
                if count[nums[j]] == 0:
                    del count[nums[j]]
                j += 1
            
            _sum += nums[i]
            count[nums[i]] = count.get(nums[i], 0) + 1
            
            if len(count) == k:
                ans = max(ans, _sum)
            
        return ans
    