class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row in range(numRows):
            curr = [1]
            for i in range(row - 1):
                curr.append(res[-1][i] + res[-1][i + 1])
            if row != 0:
                curr.append(1)
            res.append(curr)
        return res