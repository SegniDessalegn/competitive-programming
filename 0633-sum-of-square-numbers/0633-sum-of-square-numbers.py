class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 1:
            return True
        a, b = 0, int(sqrt(c))
        while a <= b:
            s = (a * a) + (b * b)
            if s < c:
                a += 1
            elif s > c:
                b -= 1
            else:
                return True
        return False