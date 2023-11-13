class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def get_sum(a1, an, n):
            return (n * (a1 + an)) // 2
        
        def good(num):
            left_space = index + 1
            right_space = n - index

            left_sum = get_sum(max(0, num - left_space) + 1, num, min(left_space, num)) + max(0, left_space - num)
            right_sum = get_sum(max(0, num - right_space) + 1, num, min(right_space, num)) + max(0, right_space - num)
            
            return left_sum + right_sum - num <= maxSum

        left = 1
        right = maxSum + 1
        while right - left > 1:
            mid = (left + right) // 2
            if good(mid):
                left = mid
            else:
                right = mid
        
        return left
