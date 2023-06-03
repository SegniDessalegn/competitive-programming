class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp
        # we have to use two states in recursion, because if we buy a stock we can't buy another one unless we sell the stock first
        
        n = len(prices)
        dp = {}
        def find_max(index, can_buy):
            if index >= n:
                return 0
            
            buy = 0
            sell = 0
            if (index, can_buy) in dp:
                return dp[(index, can_buy)]
            if can_buy:
                buy = max(find_max(index + 1, False) - prices[index], find_max(index + 1, True))
            else:
                sell = max(find_max(index + 1, True) + prices[index] - fee, find_max(index + 1, False))
            
            dp[(index, can_buy)] = max(buy, sell)
            
            return dp[(index, can_buy)]
        
        return find_max(0, True)