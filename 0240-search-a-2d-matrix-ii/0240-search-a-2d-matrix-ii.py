class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1
        while up <= down:
            middle = (up + down) // 2
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] < target:
                up = middle + 1
            else:
                down = middle - 1
        
        row = min(up, len(matrix) - 1)
        while row >= 0:
            left = 0
            right = len(matrix[0]) - 1
            while left <= right:
                middle = (left + right) // 2
                if matrix[row][middle] == target:
                    return True
                elif matrix[row][middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            row -= 1
        
        return False