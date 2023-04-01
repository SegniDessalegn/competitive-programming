class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        i = 1
        while i < len(s):
            length = 1
            while i < len(s) and s[i] == s[i - 1]:
                length += 1
                i += 1
            max_power = max(max_power, length)
            i += 1
        
        return max_power