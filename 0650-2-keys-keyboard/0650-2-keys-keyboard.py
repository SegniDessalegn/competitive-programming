class Solution:
    def minSteps(self, n: int) -> int:
        m = n // 2
        while m > 0:
            if n % m == 0:
                return (n // m) + self.minSteps(m)
            m -= 1
        return 0
