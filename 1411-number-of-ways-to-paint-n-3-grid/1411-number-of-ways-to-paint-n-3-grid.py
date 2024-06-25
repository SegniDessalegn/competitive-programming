class Solution:
    def numOfWays(self, N: int) -> int:
        valid_next = {
            0: [1, 2, 4, 5, 10],
            1: [0, 3, 6, 8, 11],
            2: [0, 3, 6, 7],
            3: [1, 2, 7, 10],
            4: [0, 6, 8, 9],
            5: [0, 6, 7, 9, 10],
            6: [1, 2, 4, 5, 11],
            7: [2, 3, 5, 11],
            8: [1, 4, 9, 10],
            9: [4, 5, 8, 11],
            10: [0, 3, 5, 8, 11],
            11: [1, 6, 7, 9, 10]
        }
        
        @cache
        def get_ans(i, prev):
            if i == 0:
                return 1
            
            curr = 0
            for B in valid_next[prev]:
                curr += get_ans(i - 1, B)
            return curr % MOD
        
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(12):
            ans += get_ans(N - 1, i)
        
        return ans % MOD
    
        