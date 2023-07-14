class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def recur(i, can_buy):
            if i >= N:
                return 0
            
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]
            
            profit = 0
            for j in range(i, N):
                if can_buy:
                    profit = max(profit, -prices[j] + recur(j + 1, False))
                else:
                    profit = max(profit, prices[j] + recur(j + 2, True))
                
            dp[(i, can_buy)] = profit
            return profit
        
        N = len(prices)
        dp = {}
        recur(0, True)
        ans = 0
        for n, can_buy in dp:
            if can_buy == True:
                ans = max(ans, dp[(n, can_buy)])
        
        return ans