class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def get_ans(i, steps_left):
            if i == -1 or i == arrLen:
                return 0
            
            if steps_left == 0:
                if i == 0:
                    return 1
                else:
                    return 0
            
            return (get_ans(i, steps_left - 1) + get_ans(i - 1, steps_left - 1) + get_ans(i + 1, steps_left - 1)) % (10 ** 9 + 7)
        
        return get_ans(0, steps)