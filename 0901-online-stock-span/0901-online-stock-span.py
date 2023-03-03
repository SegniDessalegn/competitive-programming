class StockSpanner:

    def __init__(self):
        self.mono_stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.mono_stack and self.mono_stack[-1][0] <= price:
            span += self.mono_stack.pop()[1]

        self.mono_stack.append((price, span))
        
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)