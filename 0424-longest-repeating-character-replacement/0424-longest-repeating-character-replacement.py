class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        max_freq = 0
        i, j = 0, 0
        while j < len(s):
            count[s[j]] = count.get(s[j], 0) + 1
            max_freq = max(max_freq, count[s[j]])
            while j - i + 1 - max_freq > k:
                count[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans