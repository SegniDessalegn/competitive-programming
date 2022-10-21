class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum = [[0] * (len(matrix[0]) + 1)]
        for i in range(len(matrix)):
            self.pre_sum.append([0])
            for j in range(len(matrix[i])):
                self.pre_sum[-1].append(matrix[i][j] + self.pre_sum[-1][-1] + self.pre_sum[-2][j + 1] - self.pre_sum[-2][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row1][col2 + 1] - self.pre_sum[row2 + 1][col1] + self.pre_sum[row1][col1]
