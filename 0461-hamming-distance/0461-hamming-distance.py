class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        count = 0
        while n:
            count += n & 1
            n >>= 1
        
        return count