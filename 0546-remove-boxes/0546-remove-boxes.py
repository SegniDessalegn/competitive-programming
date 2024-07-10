class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        from functools import lru_cache

        @cache
        def dp(l, r, k):
            if l > r:
                return 0
            
            # remove number at l
            res = (k * k) + dp(l + 1, r, 1)
            
            # look for number that is equal to the number at l
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    res = max(res, dp(l + 1, m - 1, 1) + dp(m, r, k + 1))

            return res

        return dp(0, len(boxes) - 1, 1)
