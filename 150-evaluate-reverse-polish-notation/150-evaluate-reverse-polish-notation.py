class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                stack.append(-stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                stack.append(int((stack.pop(len(stack) - 2)) / stack.pop()))
            else:
                stack.append(int(i))
        return stack[0]
            