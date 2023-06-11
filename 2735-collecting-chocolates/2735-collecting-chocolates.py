class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        rotations = [i * x for i in range(n)]
        
        for i in range(n):
            curr = nums[i]
            for j in range(n):
                curr = min(curr, nums[i - j])
                rotations[j] += curr
        
        return min(rotations)