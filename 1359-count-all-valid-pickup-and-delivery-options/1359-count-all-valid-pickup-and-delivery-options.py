class Solution:
    def countOrders(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i * (2 * i - 1)
            result %= (10 ** 9 + 7)
        
        return result