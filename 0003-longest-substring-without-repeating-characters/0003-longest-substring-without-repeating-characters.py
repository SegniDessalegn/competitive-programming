class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dist = set()
        left = 0
        right = 0
        ans = 0
        while right < len(s):
            while s[right] in dist:
                dist.remove(s[left])
                left += 1
            dist.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans