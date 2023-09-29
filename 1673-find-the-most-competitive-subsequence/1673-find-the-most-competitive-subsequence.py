class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        mono_stack = []
        for i in range(N):
            while mono_stack and mono_stack[-1] > nums[i] and (len(mono_stack) + N - i > k):
                mono_stack.pop()
            
            mono_stack.append(nums[i])
        
        return mono_stack[:k]