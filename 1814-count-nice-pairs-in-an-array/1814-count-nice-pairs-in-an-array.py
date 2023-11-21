class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def reverse(num):
            return int(str(num)[::-1])
        
        N = len(nums)
        prev = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(N):
            ans += prev[nums[i] - reverse(nums[i])]
            ans %= MOD
            prev[nums[i] - reverse(nums[i])] += 1
        
        return ans
    