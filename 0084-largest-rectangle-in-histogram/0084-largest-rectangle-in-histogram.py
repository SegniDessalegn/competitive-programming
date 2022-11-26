class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while mono_stack and mono_stack[-1][0] > heights[i]:
                max_area = max(max_area, mono_stack[-1][0] * (i - mono_stack[-1][1]))
                start = mono_stack.pop()[1]
            mono_stack.append((heights[i], start))
        while mono_stack:
            max_area = max(max_area, mono_stack[-1][0] * (i - mono_stack[-1][1] + 1))
            mono_stack.pop()
        return max_area