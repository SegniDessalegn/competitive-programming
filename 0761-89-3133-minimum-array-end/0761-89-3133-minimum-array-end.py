class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        i = 0
        j = 0
        while 1 << j <= n:
            if x & (1 << i) == 0:
                if n & (1 << j):
                    x |= (1 << i)
                j += 1
            i += 1
        
        return x
    