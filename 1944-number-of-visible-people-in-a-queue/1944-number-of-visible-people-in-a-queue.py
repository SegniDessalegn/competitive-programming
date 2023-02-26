class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        mono_stack = []
        answer = [0] * len(heights)
        for i in range(len(heights)):
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                last = mono_stack.pop()
                answer[last[1]] = last[2] + 1
            if mono_stack:
                mono_stack[-1][2] += 1
            mono_stack.append([heights[i], i, 0])
        
        for p in mono_stack:
            answer[p[1]] = p[2]
        
        return answer