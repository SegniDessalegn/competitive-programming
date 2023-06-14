class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        def recur(index, curr_steps):
            if (index, curr_steps) in dp:
                return dp[(index, curr_steps)]
            if curr_steps > k:
                return 0
            if curr_steps == k:
                if index == endPos:
                    return 1
                else:
                    return 0
            
            dp[(index, curr_steps)] = recur(index - 1, curr_steps + 1) + recur(index + 1, curr_steps + 1)
            return dp[(index, curr_steps)]
        
        dp = {}
        return recur(startPos, 0) % (10 ** 9 + 7)