class Solution:
    def countAsterisks(self, s: str) -> int:
        is_open = False
        count = 0
        for char in s:
            if char == "|":
                is_open = not is_open
            
            if char == "*" and not is_open:
                count += 1
        
        return count