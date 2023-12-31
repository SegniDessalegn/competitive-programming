class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        start = {}
        end = {}
        for i in range(len(s)):
            if s[i] not in start:
                start[s[i]] = i
            end[s[i]] = i
        
        ans = -1
        for c in range(26):
            char = chr(c + 97)
            if char in start:
                ans = max(ans, end[char] - start[char] - 1)
        
        return ans
    