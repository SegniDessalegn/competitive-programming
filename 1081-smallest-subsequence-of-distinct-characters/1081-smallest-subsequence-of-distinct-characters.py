class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        count = Counter(s)
        
        mono_stack = []
        prev = set()
        for char in s:
            if char not in prev:
                while mono_stack and mono_stack[-1] >= char and count[mono_stack[-1]] > 0:
                    prev.remove(mono_stack.pop())
                
                mono_stack.append(char)
                prev.add(char)
            count[char] -= 1
        
        return "".join(mono_stack)
    