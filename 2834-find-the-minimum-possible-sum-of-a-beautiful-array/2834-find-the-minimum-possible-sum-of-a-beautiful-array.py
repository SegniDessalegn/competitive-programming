class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        """
        - pick the numbers less than or equal to half of n
        - if the length is not enough, we can pick the numbers greater than or equal to n
        """
        
        def get_sum(start, length):
            return (length * (start + start + length - 1)) // 2
        
        MOD = 10 ** 9 + 7
        half = target // 2
        ans = get_sum(1, min(n, half))
        
        if n > half:
            ans += get_sum(target, n - half)
        
        return ans % MOD
        