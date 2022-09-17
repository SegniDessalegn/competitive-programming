class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        mono_stack = []
        result = ""
        for index, i in enumerate(num):
            while mono_stack and mono_stack[-1] > i:
                mono_stack.pop()
                k -= 1
                if k == 0:
                    result = "".join(mono_stack)
                    while not result and index < len(num) and num[index] == "0":
                        index += 1
                    result += num[index:]
                    return result or "0"
            if i != "0":
                mono_stack.append(i)
        return "".join(mono_stack[:-k]) or "0"