class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        INF = (1 << 32) - 1
        curr = INF
        count = 0
        for num in nums:
            curr &= num
            
            if curr == 0:
                count += 1
                curr = INF
        
        return max(1, count)