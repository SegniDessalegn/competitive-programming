class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def check(s, i):
            for j in range(i, N):
                if p[j] != "*":
                    return False
            return True
        
        @cache
        def get_ans(i, j):
            if j == N:
                return i == M
            
            if i == M:
                return check(s, j)
            
            if p[j] == "*":
                return get_ans(i, j + 1) or get_ans(i + 1, j) or get_ans(i + 1, j + 1)
            elif p[j] == "?":
                return get_ans(i + 1, j + 1)
            elif s[i] != p[j]:
                return False
            else:
                return get_ans(i + 1, j + 1)
        
        M = len(s)
        N = len(p)
        return get_ans(0, 0)
    