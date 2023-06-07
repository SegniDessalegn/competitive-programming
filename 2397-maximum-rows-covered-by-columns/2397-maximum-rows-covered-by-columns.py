class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        return self.back_track(matrix, 0, 0, numSelect)
    
    
    def back_track(self, matrix, curr_col, selected, numSelect, cols = set()):
        if selected == numSelect:
            return self.count_valid(matrix, cols)
        
        ans = 0
        for j in range(curr_col, len(matrix[0])):
            cols.add(j)
            ans = max(ans, self.back_track(matrix, j + 1, selected + 1, numSelect, cols))
            cols.discard(j)
        
        return ans
    
    
    def count_valid(self, matrix, cols):
        count = 0
        for i in range(len(matrix)):
            valid = True
            for j in range(len(matrix[0])):
                if j not in cols and matrix[i][j] == 1:
                    valid = False
                    break
            if valid:
                count += 1
        
        return count