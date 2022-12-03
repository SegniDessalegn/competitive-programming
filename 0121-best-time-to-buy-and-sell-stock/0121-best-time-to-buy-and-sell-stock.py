class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        ans = 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            ans = max(ans, prices[j] - prices[i])
            j += 1
        return ans