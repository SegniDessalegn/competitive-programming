class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def get_ans(i, j):
            if j == P:
                return i == S
            if i == S:
                return j + 1 < P and p[j + 1] == "*" and get_ans(i, j + 2)
            
            if s[i] == p[j] or p[j] == ".":
                if j < P - 1 and p[j + 1] == "*":
                    return get_ans(i, j + 2) or get_ans(i + 1, j)
                else:
                    return get_ans(i + 1, j + 1)
            
            if j + 1 < P and p[j + 1] == "*":
                return get_ans(i, j + 2)
            
            return False
        
        S = len(s)
        P = len(p)
        return get_ans(0, 0)
    