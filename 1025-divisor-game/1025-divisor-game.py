class Solution:
    def divisorGame(self, n: int) -> bool:
        
        @cache
        def canWin(n, turn):
            if n <= 1:
                return False
            
            curr = False
            for x in range(1, n):
                if n % x == 0:
                    if turn:
                        curr |= not canWin(n - x, not turn)
                    else:
                        curr |= not canWin(n - x, not turn)
            
            return curr
        
        return canWin(n, True)