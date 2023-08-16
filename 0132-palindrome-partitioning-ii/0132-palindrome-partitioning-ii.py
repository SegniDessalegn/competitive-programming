class Solution:
    def minCut(self, s: str) -> int:
        # dynamic programming
        
        N = len(s)
        is_pal = [[False for _ in range(N)] for __ in range(N)]
        for i in range(N):
            for j in range(i, N):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    is_pal[i][j] = True
        
        @cache
        def partition(start, end):
            if end == N:
                if start == N:
                    return 0
                return float("inf")
            
            count = float("inf")
            #choose
            if is_pal[start][end]:
                count = min(count, 1 + partition(end + 1, end + 1))
            
            # not choose
            count = min(count, partition(start, end + 1))
            
            return count
        
        N = len(s)
        return partition(0, 0) - 1