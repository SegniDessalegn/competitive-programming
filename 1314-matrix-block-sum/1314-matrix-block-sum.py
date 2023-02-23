class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        pref = [[0 for _ in range(len(mat[0]) + 1)]]
        for i in range(len(mat)):
            curr = [0]
            for j in range(len(mat[0])):
                curr.append(mat[i][j] + curr[j] + pref[i][j + 1] - pref[i][j])
            pref.append(curr[:])
        
        answer = [[0 for _ in range(len(mat[0]))] for __ in range(len(mat))]
        for i in range(len(answer)):
            for j in range(len(answer[0])):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(len(answer) - 1, i + k), min(len(answer[0]) - 1, j + k)
                answer[i][j] = pref[r2 + 1][c2 + 1] - pref[r2 + 1][c1] - pref[r1][c2 + 1] + pref[r1][c1]
        
        return answer