class Solution:
    def calculate(self, s: str) -> int:
        numbers = []
        operations = []
        num = ""
        i = 0
        while i < len(s):
            if s[i] in "+-*/":
                operations.append(s[i])
            num = ""
            while i < len(s) and s[i] in "0123456789":
                num += s[i]
                i+=1
            if num != "" and num != " ":
                numbers.append(int(num))
                if numbers and operations:
                    if operations[-1] == "-":
                        numbers.append(-numbers.pop())
                    elif operations[-1] == "*":
                        numbers.append(numbers.pop() * numbers.pop())
                    elif operations[-1] == "/":
                        if numbers[-1] == 0 or numbers[-2] == 0:
                            numbers.pop()
                            numbers.append(0)
                        else:
                            division = int(numbers[-2] / numbers[-1])
                            numbers.pop()
                            numbers.pop()
                            numbers.append(division)
            else:
                i += 1
        answer = 0
        for i in numbers:
            answer += i
        return answer