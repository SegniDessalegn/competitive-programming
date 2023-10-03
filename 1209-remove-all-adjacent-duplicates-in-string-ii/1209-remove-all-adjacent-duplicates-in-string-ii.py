class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                new_count = stack.pop()[1] + 1
                if new_count != k:
                    stack.append((char, new_count))
            else:
                stack.append((char, 1))
        
        return "".join([char * count for char, count in stack])