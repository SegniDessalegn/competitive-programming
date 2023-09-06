class Solution:
    def numTilings(self, n: int) -> int:
        
        @cache
        def get_ans(col):
            if col == n:
                return 1
            if col > n:
                return 0
            
            # pick 2 X 1 block
            curr_count = get_ans(col + 1) + get_ans(col + 2)
            
            # pick tromino
            for i in range(col, n):
                curr_count += 2 * get_ans(i + 3)
            
            return curr_count % (10 ** 9 + 7)
            
        return get_ans(0)