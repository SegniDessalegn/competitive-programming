class Solution:
    def countCollisions(self, directions: str) -> int:
        
        stack = []
        r_count = 0
        collisions = 0
        for d in directions:
            if d == "R":
                r_count += 1
                stack.append("R")
            elif d == "L":
                if stack and stack[-1] != "L":
                    if stack[-1] == "R":
                        stack.pop()
                        collisions += 2
                    else:
                        collisions += 1
                    stack.append("S")
                else:
                    stack.append("L")
            else:
                stack.append("S")
        
        found = False
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == "S":
                found = True
            if found and stack[i] == "R":
                collisions += 1
        
        return collisions