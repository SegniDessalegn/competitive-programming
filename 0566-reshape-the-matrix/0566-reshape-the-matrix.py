class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) == r * c:
            new_mat = []
            i = 0
            curr_row = []
            counter = 0
            while i < len(mat):
                j = 0
                while j < len(mat[i]):
                    curr_row.append(mat[i][j])
                    counter += 1
                    if counter % c == 0:
                        new_mat.append(curr_row)
                        curr_row = []
                    j += 1
                i += 1
            return new_mat
        else:
            return mat