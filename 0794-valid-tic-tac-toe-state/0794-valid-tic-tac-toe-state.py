class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        counts = {"X": 0, "O": 0}
        for row in board:
            for col in row:
                if col in counts:
                    counts[col] += 1
        
        winners = self.check_winners(board)
        if counts["X"] == counts["O"]:
            if (winners["X"] == 0 and winners["O"] == 0) or (winners["X"] == 0 and winners["O"] != 0):
                return True
            else:
                return False
        elif counts["X"] == counts["O"] + 1:
            if winners["O"] == 0:
                return True
            else:
                return False
        else:
            return False
    
    def check_winners(self, board):
        n = len(board)
        row_count = {i: {"X": 0, "O": 0} for i in range(n)}
        for i in range(n):
            for j in range(n):
                if board[i][j] != " ":
                    row_count[i][board[i][j]] += 1
        
        col_count = {i: {"X": 0, "O": 0} for i in range(n)}
        for j in range(n):
            for i in range(n):
                if board[i][j] != " ":
                    col_count[j][board[i][j]] += 1
        
        diagonal1 = {"X": 0, "O": 0}
        for i in range(n):
            if board[i][i] != " ":
                diagonal1[board[i][i]] += 1
        
        col = n - 1
        diagonal2 = {"X": 0, "O": 0}
        for i in range(n):
            if board[i][col] != " ":
                diagonal2[board[i][col]] += 1
            col -= 1
        
        winners = {"X": 0, "O": 0}
        for i in range(n):
            if row_count[i]["X"] == 3:
                winners["X"] += 1
            if row_count[i]["O"] == 3:
                winners["O"] += 1
            if col_count[i]["X"] == 3:
                winners["X"] += 1
            if col_count[i]["O"] == 3:
                winners["O"] += 1
        
        if diagonal1["X"] == 3:
            winners["X"] += 1
        if diagonal1["O"] >= 3:
            winners["O"] += 1
        if diagonal2["X"] == 3:
            winners["X"] += 1
        if diagonal2["O"] >= 3:
            winners["O"] += 1
        
        return winners