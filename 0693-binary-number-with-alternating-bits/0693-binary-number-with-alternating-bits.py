class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n:
            a = n
            n >>= 1
            if not (a & 1) ^ (n & 1):
                return False
        
        return True