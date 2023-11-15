class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        
        curr = 1
        ans = curr
        for num in arr:
            if num >= curr:
                ans = curr
                curr += 1
        
        return ans
    