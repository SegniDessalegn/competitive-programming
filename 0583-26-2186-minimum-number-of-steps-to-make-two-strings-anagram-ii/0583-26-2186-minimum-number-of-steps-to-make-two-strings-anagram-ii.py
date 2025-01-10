class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        
        ans = 0
        for i in range(26):
            char = chr(i + 97)
            ans += abs(s_count[char] - t_count[char])

        return ans
    