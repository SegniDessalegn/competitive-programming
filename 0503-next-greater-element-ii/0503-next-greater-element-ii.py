class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono_stack = []
        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            while mono_stack and mono_stack[-1][1] < n:
                ans[mono_stack.pop()[0]] = n
            mono_stack.append((i, n))
        for i, n in enumerate(nums):
            while mono_stack and mono_stack[-1][1] < n:
                ans[mono_stack.pop()[0]] = n
            mono_stack.append((i, n))
        return ans