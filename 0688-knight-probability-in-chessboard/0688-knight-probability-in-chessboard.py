class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        
        @cache
        def recur(move, i, j):
            if not (0 <= i < n and 0 <= j < n):
                return 0
            
            if move == 0:
                return 1
            
            count = 0
            for dx, dy in directions:
                r, c = i + dx, j + dy
                if (0 <= r < n and 0 <= c < n):
                    count += 1
            
            curr_p = 0
            for dx, dy in directions:
                r, c = i + dx, j + dy
                curr_p += (count * recur(move - 1, r, c))
            
            return 0 if count == 0 else curr_p / (count * 8)
        
        return recur(k, row, column)