class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        j = 1
        while j < len(prices):
            i = j
            while j < len(prices) and prices[j - 1] - prices[j] == 1:
                j += 1
            n += ((j - i + 1)*(j - i)//2)
            j += 1
        return n