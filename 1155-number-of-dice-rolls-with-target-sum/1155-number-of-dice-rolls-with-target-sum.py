class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        
        @cache
        def func(i, t):
            if t < 0:
                return 0
            elif i == n and t == 0:
                return 1
            elif i == n:
                return 0
            return sum([func(i + 1, t - x) for x in range(1, k + 1)])
        
        return func(0, target) % mod
    