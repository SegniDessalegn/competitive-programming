class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def count_neighbours(x, y):
            count = 0
            for r, c in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1)]:
                if 0 <= r < row and 0 <= c < col:
                    if board[r][c] is "M":
                        count += 1
            return count
        
        row = len(board)
        col = len(board[0])
        i, j = click
        if board[i][j] is "M":
            board[i][j] = "X"
            return board
        
        queue = deque([(i, j)])
        while queue:
            x, y = queue.pop()
            count = count_neighbours(x, y)
            board[x][y] = str(count)
            if count != 0:
                continue
            board[x][y] = "B"
            for r, c in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1)]:
                if 0 <= r < row and 0 <= c < col:
                    if board[r][c] is "E":
                        queue.append((r, c))
        
        return board