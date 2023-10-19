class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        N = len(s)
        numbers = []
        operations = []
        i = 0
        while i < N:
            if s[i] in "+-*/":
                operations.append(s[i])
                i += 1
                continue
            
            num = []
            while i < N and s[i] in "0123456789":
                num.append(s[i])
                i+=1
            
            numbers.append(int("".join(num)))
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
        
        answer = 0
        for num in numbers:
            answer += num
        
        return answer
    