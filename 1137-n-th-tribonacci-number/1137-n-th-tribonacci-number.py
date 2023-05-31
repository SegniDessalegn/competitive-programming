class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def recur(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            return recur(n - 1) + recur(n - 2) + recur(n - 3)
        
        return recur(n)