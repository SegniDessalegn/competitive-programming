class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mono_stack = []
        for i in range(len(arr)):
            while mono_stack and mono_stack[-1][0] < arr[i]:
                mono_stack.pop()
            mono_stack.append((arr[i], i))
        res = []
        i = 0
        for n in mono_stack:
            while i < n[1]:
                res.append(n[0])
                i += 1
        res.append(-1)
        return res