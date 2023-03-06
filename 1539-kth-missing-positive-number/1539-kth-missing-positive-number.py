class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = -1
        right = len(arr)
        while right - left > 1:
            mid = (right + left) // 2
            if arr[mid] - mid <= k:
                left = mid
            else:
                right = mid
        
        if left == -1:
            return k
        else:
            return arr[left] + (k - (arr[left] - (left + 1)))