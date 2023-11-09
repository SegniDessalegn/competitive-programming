class Solution:
    def countHomogenous(self, s: str) -> int:
        s += "#"
        MOD = 10 ** 9 + 7
        N = len(s)
        ans = 0
        curr_length = 1
        for i in range(1, N):
            if s[i] == s[i - 1]:
                curr_length += 1
            else:
                ans += (curr_length * (curr_length + 1)) // 2
                ans %= MOD
                curr_length = 1
        
        return ans
    