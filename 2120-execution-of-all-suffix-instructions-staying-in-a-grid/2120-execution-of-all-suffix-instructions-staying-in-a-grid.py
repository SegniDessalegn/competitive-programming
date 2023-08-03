class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
        
        def traverse(row, column, i):
            if i == len(s):
                return 0
            
            dx, dy = directions[s[i]]
            
            new_row = row + dx
            new_column = column + dy
            
            if not (0 <= new_row < n and 0 <= new_column < n):
                return 0
            
            return 1 + traverse(new_row, new_column, i + 1)
        
        instructions = []
        for i in range(len(s)):
            instructions.append(traverse(startPos[0], startPos[1], i))
        
        return instructions