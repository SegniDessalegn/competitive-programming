class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def recur(i, can_buy, transactions):
            if i >= N or transactions >= 2:
                return 0
            
            profit = 0
            if can_buy:
                profit = max(profit, recur(i + 1, True, transactions), -prices[i] + recur(i + 1, False, transactions))
            else:
                profit = max(profit, recur(i + 1, False, transactions), prices[i] + recur(i + 1, True, transactions + 1))
                
            return profit
        
        N = len(prices)
        return recur(0, True, 0)
    