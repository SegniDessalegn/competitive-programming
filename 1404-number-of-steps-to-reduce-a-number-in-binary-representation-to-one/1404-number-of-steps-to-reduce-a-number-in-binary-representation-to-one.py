class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        ops = 0
        while num != 1:
            if num & 1:
                num += 1
            else:
                num >>= 1
            ops += 1
        
        return ops