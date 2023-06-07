class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        cups = [[poured]]
        for i in range(1, query_row + 1):
            cups.append([0 for _ in range(i + 1)])
            for j in range(i + 1):
                if j != 0 and cups[i - 1][j - 1] > 1:
                    cups[i][j] += (cups[i - 1][j - 1] - 1) / 2
                if j != i and cups[i - 1][j] > 1:
                    cups[i][j] += (cups[i - 1][j] - 1) / 2
        
        return min(1.0, cups[query_row][query_glass])