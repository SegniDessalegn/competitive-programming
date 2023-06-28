class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        evens = pow(5, (n + 1) // 2, MOD)
        primes = pow(4, n // 2, MOD)
        return (evens * primes) % MOD
        