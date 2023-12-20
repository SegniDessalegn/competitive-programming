class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        left = money - sum(prices[:2])
        return left if left >= 0 else money
    