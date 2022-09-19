class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.isPowerOfThree(n / 3) if n > 1 else True if n == 1 else False