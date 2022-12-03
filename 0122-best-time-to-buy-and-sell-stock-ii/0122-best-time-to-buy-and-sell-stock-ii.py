class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit += p - min_price
                min_price = p
        return profit