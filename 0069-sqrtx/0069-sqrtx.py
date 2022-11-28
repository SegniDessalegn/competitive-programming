class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            curr = left + ((right - left) // 2)
            if curr * curr > x:
                right = curr - 1
            elif curr * curr < x:
                left = curr + 1
            else:
                return curr
        return left - 1