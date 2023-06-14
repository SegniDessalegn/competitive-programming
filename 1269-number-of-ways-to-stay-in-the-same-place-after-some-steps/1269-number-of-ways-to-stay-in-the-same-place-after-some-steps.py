class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        def recur(index, curr_steps):
            if (index, curr_steps) in dp:
                return dp[(index, curr_steps)]
            if index < 0 or index >= arrLen:
                return 0
            if curr_steps == steps:
                if index == 0:
                    return 1
                else:
                    return 0
            
            dp[(index, curr_steps)] = recur(index - 1, curr_steps + 1) + recur(index, curr_steps + 1) + recur(index + 1, curr_steps + 1)
            return dp[(index, curr_steps)]
        
        dp = {}
        return recur(0, 0) % (10 ** 9 + 7)