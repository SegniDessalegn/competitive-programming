class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        count = {i:0 for i in p}
        ans = []
        chars = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] in count:
                count[s[j]] += 1
                if count[s[j]] <= p_count[s[j]]:
                    chars += 1
            if j >= len(p) and s[i] in count:
                count[s[i]] -= 1
                chars -= 1
                if count[s[i]] >= p_count[s[i]]:
                    chars += 1
            if chars == len(p):
                ans.append(j - len(p) + 1)
            if j >= len(p):
                i += 1
            j += 1
        return ans