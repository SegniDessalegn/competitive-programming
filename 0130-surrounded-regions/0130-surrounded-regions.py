class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        queue = deque()
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i, j) not in visited:
                    queue.append((i, j))
                    curr_visited = set([(i, j)])
                    surrounded = True
                    while queue:
                        x, y = queue.popleft()
                        for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if 0 <= r < row and 0 <= c < col:
                                if board[r][c] == "O" and (r, c) not in curr_visited:
                                    queue.append((r, c))
                                    curr_visited.add((r, c))
                            else:
                                surrounded = False
                    for r, c in curr_visited:
                        if surrounded:
                            board[r][c] = "X"
                        visited.add((r, c))