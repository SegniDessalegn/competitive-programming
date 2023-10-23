class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1 or n & (n - 1):
            return False
        
        return (int(math.log(n, 2)) + 1) % 2 != 0
        