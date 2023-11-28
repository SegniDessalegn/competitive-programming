class Solution:
    def numberOfWays(self, corridor: str) -> int:
        N = len(corridor)
        MOD = 10 ** 9 + 7
        ans = 1
        
        count = 0
        left = corridor.count("S")
        if left % 2 != 0 or N < 2 or left == 0:
            return 0
        
        streak = 0
        for i in range(N):
            if corridor[i] == "S":
                count += 1
                left -= 1
            
            if count == 2:
                streak += 1
            
            elif count < 2:
                if streak > 0:
                    ans *= streak
                streak = 0
            else:
                if streak > 0:
                    ans *= streak
                count = 1
                streak = 0
            ans %= MOD
        
        return ans
    