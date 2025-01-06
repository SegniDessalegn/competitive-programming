class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, j, w, visited):
            if w == W:
                return True
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == word[w] and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    if backtrack(ni, nj, w + 1, visited):
                        return True
                    visited.discard((ni, nj))

            return False
        
        M = len(board)
        N = len(board[0])
        W = len(word)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 1, set([(i, j)])):
                        return True

        return False
    