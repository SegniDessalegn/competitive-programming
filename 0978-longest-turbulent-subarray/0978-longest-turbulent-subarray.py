class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        def invalid(right):
            if arr[right - 2] > arr[right - 1]:
                return arr[right - 1] >= arr[right]
            else:
                return arr[right - 1] <= arr[right]
        
        N = len(arr)
        left = 0
        ans = 1
        for right in range(1, N):
            if right - left + 1 == 1:
                continue
            if arr[right] == arr[right - 1]:
                left = right
            elif right - left + 1 > 2 and invalid(right):
                left = right - 1
            
            ans = max(ans, right - left + 1)
        
        return ans
    