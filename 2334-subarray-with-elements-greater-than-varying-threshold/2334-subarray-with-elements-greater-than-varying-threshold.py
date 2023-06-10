class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [i for i in range(n)]
        mono_stack = []
        for i in range(len(nums)):
            while mono_stack and nums[mono_stack[-1]] >= nums[i]:
                left[i] = left[mono_stack.pop()]
            mono_stack.append(i)
        
        right = [i for i in range(n)]
        mono_stack = []
        for i in range(n - 1, -1, -1):
            while mono_stack and nums[mono_stack[-1]] >= nums[i]:
                right[i] = right[mono_stack.pop()]
            mono_stack.append(i)
        
        for i in range(n):
            length = right[i] - left[i] + 1
            if nums[i] > threshold / length:
                return length
        
        return -1