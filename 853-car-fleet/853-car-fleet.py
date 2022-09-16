class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_time = [(i,(target - i)/j) for i,j in zip(position, speed)]
        position_time.sort(reverse = True)
        mono_stack = []
        answer = 1
        for _, time in position_time:
            while mono_stack and mono_stack[-1] < time:
                mono_stack.pop()
                if len(mono_stack) == 0:
                    answer += 1
            mono_stack.append(time)
        return answer