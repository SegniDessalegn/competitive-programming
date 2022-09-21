class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n > 0:
            if n % 2 == 0:
                result = self.myPow(x, n / 2)
                if n < 0 and result != 0:
                    result = 1 / result
                return result * result
            else:
                return x * self.myPow(x, n - 1)
            
        else:
            return 1 / self.myPow(x, -n)