class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        @cache
        def dp(i, j):
            if i == j:
                return 0

            min_cost = float('inf')
            for k in range(i, j):
                left_cost = dp(i, k)
                right_cost = dp(k+1, j)
                max_left = max(arr[i: k + 1])
                max_right = max(arr[k+1: j + 1])
                min_cost = min(min_cost, left_cost + right_cost + max_left * max_right)

            return min_cost

        N = len(arr)
        return dp(0, N - 1)
    