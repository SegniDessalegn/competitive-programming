class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n + 1
        while right - left > 1:
            mid = left + (right - left) // 2
            if mid <= citations[n - mid]:
                left = mid
            else:
                right = mid
        
        return left