class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        freq = {}
        while right != len(s):
            if s[right] not in freq.keys() or right == left:
                freq[s[right]] = 1
                right += 1
            else:
                freq.pop(s[left])
                left += 1
            if right - left > longest:
                longest = right - left
        return longest