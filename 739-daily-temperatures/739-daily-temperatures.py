class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while mono_stack and mono_stack[-1][0] < temperatures[i]:
                index = mono_stack.pop()[1]
                answer[index] = i - index
            mono_stack.append((temperatures[i], i))
        return answer