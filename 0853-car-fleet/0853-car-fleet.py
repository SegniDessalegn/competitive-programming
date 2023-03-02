class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort()
        
        mono_stack = []
        for i in range(len(cars)):
            while mono_stack and mono_stack[-1][1] > cars[i][1] and (target - cars[i][0]) / cars[i][1] >= (target - mono_stack[-1][0]) / mono_stack[-1][1]:
                mono_stack.pop()
            mono_stack.append(cars[i])
        
        return len(mono_stack)