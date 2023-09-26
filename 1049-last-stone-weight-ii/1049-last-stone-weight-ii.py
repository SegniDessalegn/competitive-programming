class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        @cache
        def get_ans(i, group1, group2):
            
            if i >= N:
                return abs(group1 - group2)
            
            return min(get_ans(i + 1, group1 + stones[i], group2), get_ans(i + 1, group1, group2 + stones[i]))
        
        N = len(stones)
        return get_ans(0, 0, 0)