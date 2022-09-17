class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        p1 = 0
        p2 = 0
        stack = []
        while True:
            if p1 == len(pushed) - 1:
                if popped[p2 + 1::] == stack[::-1]:
                    return True
                else:
                    return False
            stack.append(pushed[p1])
            p1 += 1
            while stack[-1] == popped[p2]:
                stack.pop()
                p2 += 1
                if p2 == len(popped) - 1:
                    return True
                if not stack:
                    break