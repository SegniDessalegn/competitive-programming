class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backTracking(i, j, curr_ans, visited):
            if len(curr_ans) == len(word):
                return True
            
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n:
                    if word[len(curr_ans)] != board[x][y] or (x, y) in visited:
                        continue
                    curr_ans.append(board[x][y])
                    visited.add((x, y))
                    if backTracking(x, y, curr_ans, visited):
                        return True
                    curr_ans.pop()
                    visited.remove((x, y))
        
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backTracking(i, j, [word[0]], set([(i, j)])):
                    return True
        
        return False