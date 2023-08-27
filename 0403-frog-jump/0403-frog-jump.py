class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        @cache
        def get_ans(i, prev):
            if i == N - 1:
                return True
            
            for j in range(-1, 2):
                new_pos = stones[i] + prev + j
                idx = bisect_left(stones, new_pos)
                if i < idx < N and stones[idx] == new_pos and get_ans(idx, prev + j):
                    return True
            
            return False
        
        N = len(stones)
        return get_ans(0, 0)
    