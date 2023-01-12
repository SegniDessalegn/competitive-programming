class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            ver = top + ((bot - top + 1) // 2)
            if matrix[ver][0] > target:
                bot = ver - 1
            elif matrix[ver][0] < target:
                top = ver + 1
            else:
                return True
            
        left, right = 0, len(matrix[bot]) - 1
        while left <= right:
            hor = left + ((right - left + 1) // 2)
            if matrix[bot][hor] > target:
                right = hor - 1
            elif matrix[bot][hor] < target:
                left = hor + 1
            else:
                return True
        return False
    