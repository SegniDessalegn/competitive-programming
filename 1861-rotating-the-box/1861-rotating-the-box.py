class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        for i in range(m):
            curr = 0
            for j in range(n):
                if box[i][j] == ".":
                    box[i][j], box[i][curr] = box[i][curr], box[i][j]
                    curr += 1
                elif box[i][j] == "*":
                    curr = j + 1
        
        mat = [[None for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                mat[j][i] = box[-i - 1][j]
        
        return mat