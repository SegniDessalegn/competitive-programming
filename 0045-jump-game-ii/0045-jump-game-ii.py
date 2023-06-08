class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        start = far = 0
        n = len(nums)
        for i in range(n):
            if i + nums[i] > far:
                far = i + nums[i]
            if i == start and i != n - 1:
                steps += 1
                start = far
        
        return steps