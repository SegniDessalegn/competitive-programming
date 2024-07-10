class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]

        @cache
        def merge_cost(i, j):
            if i == j:
                return 0
            min_cost = float('inf')
            for m in range(i, j, K - 1):
                min_cost = min(min_cost, merge_cost(i, m) + merge_cost(m + 1, j))
            if (j - i) % (K - 1) == 0:
                min_cost += prefix_sum[j + 1] - prefix_sum[i]
            return min_cost
        
        return merge_cost(0, n - 1)
    