class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            curr = left + ((right - left) // 2)
            if curr * curr > num:
                right = curr - 1
            elif curr * curr < num:
                left = curr + 1
            else:
                return True
        return False