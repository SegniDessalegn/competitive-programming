class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mono_stack = []
        min_nums = []
        curr_min = nums[0]
        for i in range(len(nums)):
            min_nums.append(curr_min)
            if nums[i] < curr_min:
                curr_min = nums[i]
            while mono_stack and mono_stack[-1][0] <= nums[i]:
                mono_stack.pop()
            mono_stack.append((nums[i], i))
            if len(mono_stack) >= 2 and min_nums[mono_stack[-2][1]] < mono_stack[-1][0]:
                return True
        return False
        