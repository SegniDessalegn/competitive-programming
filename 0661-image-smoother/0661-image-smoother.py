class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        M = len(img)
        N = len(img[0])
        
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        def get_avg(i, j):
            s = 0
            n = 0
            for dx, dy in neighbours:
                r, c = i + dx, j + dy
                if 0 <= r < M and 0 <= c < N:
                    s += img[r][c]
                    n += 1
            
            return s// n
            
        ans = [[0] * N for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                ans[i][j] = get_avg(i, j)
        
        return ans
    