class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_length = 1
        left = 0
        right = 1
        while right < len(s):
            if ord(s[right]) - ord(s[right - 1]) == 1:
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                left = right
                right += 1
            if max_length == 26:
                break
        
        return max_length