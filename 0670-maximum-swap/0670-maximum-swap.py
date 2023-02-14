class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        mono_stack = []
        for i in range(len(num)):
            while mono_stack and int(mono_stack[-1][0]) < int(num[i]):
                mono_stack.pop()
            mono_stack.append((num[i], i))
        
        for i in range(len(mono_stack)):
            index = mono_stack[i][1]
            if i != index:
                p = i
                while i < len(mono_stack) - 1 and mono_stack[i][0] == mono_stack[i + 1][0]:
                    i += 1
                num[p], num[mono_stack[i][1]] = num[mono_stack[i][1]], num[p]
                break
        
        return int("".join(num))