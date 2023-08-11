class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def back_track(i, curr):
            if curr > amount:
                return 0
            if curr == amount:
                return 1
            
            count = 0
            for j in range(i, n):
                count += back_track(j, curr + coins[j])
            
            return count
        
        n = len(coins)
        return back_track(0, 0)