class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        N = len(nums)
        robots = []
        for i in range(N):
            if s[i] == "R":
                robots.append(nums[i] + d)
            else:
                robots.append(nums[i] - d)
        
        robots.sort()
        
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(1, N):
            ans += (robots[i] - robots[i - 1]) * ((N - i) * i)
            ans %= MOD
        
        return ans
    