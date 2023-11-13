class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        sv = []
        for char in s:
            if char in vowels:
                sv.append(char)
        
        sv.sort()
        
        ans = s[:]
        i = 0
        p = 0
        while i < len(ans):
            while i < len(ans) and ans[i] not in vowels:
                i += 1
            if i < len(ans):
                ans[i] = sv[p]
            p += 1
            i += 1
        
        return "".join(ans)