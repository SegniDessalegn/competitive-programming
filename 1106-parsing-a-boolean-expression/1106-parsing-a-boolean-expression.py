class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        def operation(arr):
            if arr[0] == "!":
                return arr[1] == "f"
            
            result = arr[0] == "&"
            for i in range(1, len(arr)):
                if arr[0] == "&":
                    result = result and arr[i] == "t"
                else:
                    result = result or arr[i] == "t"
            return result
        
        stack = []
        for i in range(len(expression)):
            if expression[i] == ")":
                idx = 0
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j] == "!" or stack[j] == "&" or stack[j] == "|":
                        idx = j
                        break
                curr = operation(stack[idx:])
                while len(stack) != idx:
                    stack.pop()
                stack.append("t" if curr else "f")
            elif expression[i] != "(" and expression[i] != ",":
                stack.append(expression[i])
            
        return stack[0] == "t"
    