class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        level = 0
        while level < len(matrix) // 2:
            up, below = self.get_rows(matrix, level)
            left, right = self.get_cols(matrix, level)
            left = left[::-1]
            right = right[::-1]
            for i in range(len(left)):
                matrix[level][i + level] = left[i]
                matrix[len(matrix) - 1 - level][i + level] = right[i]
            
            for i in range(len(up)):
                matrix[i + level][level] = below[i]
                matrix[i + level][len(matrix) - 1 - level] = up[i]
            level += 1
            
    def get_rows(self, matrix, level):
        return (matrix[level][level:len(matrix) - level], matrix[len(matrix) - 1 - level][level:len(matrix) - level])

    def get_cols(self, matrix, level):
        left = []
        right = []
        for i in range(level, len(matrix) - level):
            for j in range(level, len(matrix) - level):
                if j == level:
                    left.append(matrix[i][j])
                if j == len(matrix) - level - 1:
                    right.append(matrix[i][j])
        return (left, right)