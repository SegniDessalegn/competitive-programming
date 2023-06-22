class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            last_bit = c & 1
            if last_bit == 1:
                if ((a & 1) or (b & 1)) == 0:
                    flips += 1
            else:
                if a & 1 == 1:
                    flips += 1
                if b & 1 == 1:
                    flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips