class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        next_smaller = [p for p in prices]
        
        mono_stack = []
        for i in range(N):
            while mono_stack and prices[mono_stack[-1]] >= prices[i]:
                index = mono_stack.pop()
                next_smaller[index] = prices[index] - prices[i]
            mono_stack.append(i)
        
        return next_smaller