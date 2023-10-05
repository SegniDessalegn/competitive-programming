class Solution:
    def knightDialer(self, n: int) -> int:
        
        @cache
        def get_ans(curr_n, num):
            if curr_n == 0:
                return 1
            
            curr_count = 0
            
            for nxt in go_to[num]:
                curr_count += get_ans(curr_n - 1, nxt)
            
            return curr_count % MOD
        
        if n == 1:
            return 10
        
        MOD = 10 ** 9 + 7
        go_to = {1:(6, 8), 2:(7, 9), 3:(4, 8), 4: (0, 3, 9), 6:(1, 7, 0), 7:(2, 6), 8:(1, 3), 9:(2, 4), 0:(4, 6)}
        count = 0
        for start in range(10):
            if start != 5:
                count += get_ans(n - 1, start)
        
        return count % MOD