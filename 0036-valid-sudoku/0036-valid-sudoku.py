class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = {i:set() for i in range(len(board))}
        col_count = {i:set() for i in range(len(board))}
        little_squares = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                n = board[row][col]
                if n != ".":
                    if n in row_count[row] or n in col_count[col]:
                        return False
                    else:
                        row_count[row].add(n)
                        col_count[col].add(n)
                    if (row // 3, col // 3) not in little_squares:
                        little_squares[(row // 3, col // 3)] = set()
                    if n in little_squares[(row // 3, col // 3)]:
                        return False
                    little_squares[(row // 3, col // 3)].add(n)
        return True