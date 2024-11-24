class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        
        @cache
        def get_ans(i, k, started):
            if k == 0:
                return 1
            if i == n:
                return 0
            
            count = get_ans(i + 1, k, started)
            
            if started:
                count += get_ans(i + 1, k, False)
            else:
                count += get_ans(i, k - 1, True)
            
            return count % MOD
        
        MOD = 1000000007
        return get_ans(0, k, True)
    