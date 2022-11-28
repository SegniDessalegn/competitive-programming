class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        curr = 1
        while curr <= n:
            curr += row + 1
            row += 1
        return row - 1