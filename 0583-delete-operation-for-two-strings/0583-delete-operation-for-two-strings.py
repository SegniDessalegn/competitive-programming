class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)
        
        @cache
        def find_ans(i, j):
            if i == N1 or j == N2:
                return max(N1 - i, N2 - j)
            
            curr_ans = N1 + N2
            curr_ans = min(curr_ans, 1 + find_ans(i + 1, j), 1 + find_ans(i, j + 1))
            if word1[i] == word2[j]:
                curr_ans = min(curr_ans, find_ans(i + 1, j + 1))
            
            return curr_ans
        
        return find_ans(0, 0)
    