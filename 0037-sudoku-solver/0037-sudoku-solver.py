class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def is_valid(board, row, col, num):
            for i in range(9):
                if board[i][col] == num:
                    return False

            for j in range(9):
                if board[row][j] == num:
                    return False

            for i in range(3):
                for j in range(3):
                    if board[3 * (row // 3) + i][3 * (col // 3) + j] == num:
                        return False
            
            return True


        def backTrack(i):
            if i == 81:
                return True

            row = i // 9
            col = i % 9

            if board[row][col] == ".":
                for num in range(1, 10):
                    if is_valid(board, row, col, str(num)):
                        board[row][col] = str(num)
                        if backTrack(i + 1):
                            return True
                        board[row][col] = "."
                return False
            else:
                return backTrack(i + 1)
        
        
        backTrack(0)