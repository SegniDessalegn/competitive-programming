class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        matchsticks.sort()
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        side = s // 4
        
        @cache
        def get_ans(mask, curr):
            if mask == (1 << N) - 1:
                return curr == 0
            
            for i in range(N):
                length = curr + matchsticks[i]
                if not ((1 << i) & mask) and length <= side:
                    length = 0 if length == side else length
                    if get_ans(mask | (1 << i), length):
                        return True
            
            return False
        
        return get_ans(0, 0)