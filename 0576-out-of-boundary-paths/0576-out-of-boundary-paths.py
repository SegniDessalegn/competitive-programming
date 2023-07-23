class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        @cache
        def recur(move, i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 1
            
            if move == 0:
                return 0
            
            count = 0
            for dx, dy in directions:
                r, c = i + dx, j + dy
                count += recur(move - 1, r, c)
            
            return count % (10 ** 9 + 7)
        
        return recur(maxMove, startRow, startColumn)