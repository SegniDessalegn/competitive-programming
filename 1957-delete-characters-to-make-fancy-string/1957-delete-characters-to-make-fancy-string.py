class Solution:
    def makeFancyString(self, s: str) -> str:
        
        s = list(s)
        i = 2
        for j in range(2, len(s)):
            if s[j] != s[i - 1] or s[j] != s[i - 2]:
                s[i] = s[j]
                i += 1
        
        while i < len(s):
            s[i] = ""
            i += 1
            
        return "".join(s)
    