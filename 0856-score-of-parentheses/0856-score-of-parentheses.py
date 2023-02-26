class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for p in s:
            if p == "(":
                stack.append((p, 0))
            else:
                if len(stack) > 1:
                    curr_score = stack.pop()[1]
                    if curr_score == 0:
                        curr_score = 1
                    else:
                        curr_score *= 2
                    stack[-1] = (stack[-1][0], stack[-1][1] + curr_score)
                else:
                    if stack[-1][1] == 0:
                        score += 1
                    else:
                        score += 2 * stack[-1][1]
                    stack.pop()
        
        return score