class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = {i:j for j, i in enumerate(nums1)}
        mono_stack = []
        answer = [-1] * len(nums1)
        for i in nums2:
            while mono_stack and mono_stack[-1] < i:
                temp = mono_stack.pop()
                if temp in indexes:
                    answer[indexes[temp]] = i
            mono_stack.append(i)
        return answer
        