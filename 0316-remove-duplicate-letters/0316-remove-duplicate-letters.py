class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        mono_stack = []
        used = set()
        for char in s:
            if char not in used:
                while mono_stack and count[mono_stack[-1]] != 0 and mono_stack[-1] > char:
                    used.remove(mono_stack.pop())
                used.add(char)
                mono_stack.append(char)
            count[char] -= 1
        
        return "".join(mono_stack)