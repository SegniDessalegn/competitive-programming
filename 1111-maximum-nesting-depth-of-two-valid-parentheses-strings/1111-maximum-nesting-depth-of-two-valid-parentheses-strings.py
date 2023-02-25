class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []
        answer = []
        for s in seq:
            if s == "(":
                if not stack or stack[-1][1] == 1:
                    curr = 0
                else:
                    curr = 1
                stack.append((s, curr))
                answer.append(curr)
            else:
                answer.append(stack.pop()[1])
        
        return answer
                