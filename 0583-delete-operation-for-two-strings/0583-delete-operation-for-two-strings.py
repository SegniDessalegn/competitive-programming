class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)
        
        table = [[float("inf")] * (N2 + 1) for i in range(N1 + 1)]
        table[0][0] = 0
        
        for i in range(1, N1 + 1):
            table[i][0] = table[i - 1][0] + 1

        for j in range(1, N2 + 1):
            table[0][j] = table[0][j - 1] + 1
        
        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                table[i][j] = min(table[i][j], 1 + table[i][j - 1], 1 + table[i - 1][j])
        
        return table[-1][-1]
    