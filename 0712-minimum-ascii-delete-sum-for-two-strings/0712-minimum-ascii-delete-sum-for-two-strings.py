class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N1 = len(s1)
        N2 = len(s2)
        
        @cache
        def get_ans(i, j):
            if i == N1:
                curr_ans = 0
                for k in range(j, N2):
                    curr_ans += ord(s2[k])
                return curr_ans
            elif j == N2:
                curr_ans = 0
                for k in range(i, N1):
                    curr_ans += ord(s1[k])
                return curr_ans
            
            # make them equal here
            curr_ans = float("inf")
            
            # delete from s1 or s2
            curr_ans = min(curr_ans, ord(s1[i]) + get_ans(i + 1, j))
            curr_ans = min(curr_ans, ord(s2[j]) + get_ans(i, j + 1))
            
            # skip both
            if s1[i] == s2[j]:
                curr_ans = min(curr_ans, get_ans(i + 1, j + 1))
            
            return curr_ans
        
        return get_ans(0, 0)
    