class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        mapped = set()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if t[i] not in char_map:
                if s[i] in mapped:
                    return False
                char_map[t[i]] = (s[i])
                mapped.add(s[i])
            elif s[i] != char_map[t[i]]:
                return False
        return True