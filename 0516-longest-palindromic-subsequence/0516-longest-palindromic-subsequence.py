class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def get_ans(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            
            if s[i] == s[j]:
                return 2 + get_ans(i + 1, j - 1)            
            return max(get_ans(i + 1, j), get_ans(i, j - 1))
        
        return get_ans(0, len(s) - 1)