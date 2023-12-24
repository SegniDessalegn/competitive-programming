class Solution:
    def minOperations(self, s: str) -> int:
        c1 = 0
        c2 = 1
        op1 = 0
        op2 = 0
        
        for i in range(len(s)):
            if s[i] != str(c1):
                op1 += 1
            if s[i] != str(c2):
                op2 += 1
            
            c1 += 1
            c1 %= 2
            c2 += 1
            c2 %= 2
        
        return min(op1, op2)
    