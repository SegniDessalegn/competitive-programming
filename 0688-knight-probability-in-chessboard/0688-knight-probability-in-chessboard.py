class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        
        @cache
        def recur(move, i, j):
            if not (0 <= i < n and 0 <= j < n):
                return 0
            
            if move == k:
                return 1
            
            p = 0
            for dx, dy in directions:
                r, c = i + dx, j + dy
                p += recur(move + 1, r, c)
            
            return p / 8
        
        return recur(0, row, column)