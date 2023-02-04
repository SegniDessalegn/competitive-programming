class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = 0
        for char in s:
            if char == t[p]:
                p += 1
                if p >= len(t):
                    break
        return len(t) - p