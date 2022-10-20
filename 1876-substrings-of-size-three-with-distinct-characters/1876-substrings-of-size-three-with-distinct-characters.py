class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i, j = 0, 0
        ans = 0
        count = {}
        while j < len(s):
            count[s[j]] = count.get(s[j], 0) + 1
            if j >= 2:
                if count[s[i]] == count[s[i + 1]] == count[s[i + 2]] == 1:
                    ans += 1
                count[s[i]] -= 1
                i += 1
            j += 1
        return ans