class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # choose or not choose
        N = len(strs)
        for i in range(N):
            strs[i] = [strs[i].count("0"), strs[i].count("1")]
        
        @cache
        def find_ans(i, cm, cn):
            if cm > m or cn > n:
                return -float("inf")
            if i == N:
                return 0
            
            # take this
            take = 0
            if cm + strs[i][0] <= m and cn + strs[i][1] <= n:
                take = 1 + find_ans(i + 1, cm + strs[i][0], cn + strs[i][1])
            
            # don't take this
            not_take = find_ans(i + 1, cm, cn)
            
            return max(take, not_take)
        
        
        return find_ans(0, 0, 0)
    