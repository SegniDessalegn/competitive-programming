class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        
        if i == len(s):
            return 0
        
        is_positive = None
        if s[i] == "+":
            is_positive = True
            i += 1
        elif s[i] == "-":
            is_positive = False
            i += 1
        
        while i < len(s) and s[i] == "0":
            i += 1
        
        numbers = []
        while i < len(s) and s[i] in "0123456789":
            numbers.append(s[i])
            i += 1
        
        result = 0
        for i in range(len(numbers)):
            result += int(numbers[i]) * (10 ** (len(numbers) - i - 1))
        
        result *= (1 if is_positive is None or is_positive else -1)

        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        if result < -2 ** 31:
            result = -2 ** 31
        
        return result
    