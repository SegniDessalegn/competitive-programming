class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        nums = sorted([a, b, c])
        a, b, c = nums
        if b - a == 1 and c - b == 1:
            min_moves = 0
            max_moves = 0
        elif b - a == 1 and c - b > 1:
            min_moves = 1
            max_moves = c - b - 1
        elif c - b == 1 and b - a > 1:
            min_moves = 1
            max_moves = b - a - 1
        else:
            min_moves = min(2, b - a - 1, c - b - 1)
            max_moves = b - a - 1 + c - b - 1
        
        return [min_moves, max_moves]