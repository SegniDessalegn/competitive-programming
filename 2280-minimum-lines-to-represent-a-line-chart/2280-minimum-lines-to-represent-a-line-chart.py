class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        N = len(stockPrices)
        if N == 1:
            return 0
        
        stockPrices.sort()
        count = 1
        prev_dx = stockPrices[1][0] - stockPrices[0][0]
        prev_dy = stockPrices[1][1] - stockPrices[0][1]
        for i in range(1, N):
            curr_dx = stockPrices[i][0] - stockPrices[i - 1][0]
            curr_dy = stockPrices[i][1] - stockPrices[i - 1][1]
            if prev_dx * curr_dy != prev_dy * curr_dx:
                count += 1
                prev_dx = curr_dx
                prev_dy = curr_dy
            
        return count