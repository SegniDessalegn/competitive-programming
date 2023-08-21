class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        factors = []
        for i in range(1, (N // 2) + 1):
            if N % i == 0:
                factors.append(i)
        
        for factor in factors:
            sbstr = s[:factor]
            valid = True
            for i in range(factor, N + 1, factor):
                if s[i - factor:i] != sbstr:
                    valid = False
                    break
            
            if valid:
                return True
        
        return False