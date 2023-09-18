class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i in range(len(mat)):
            heapq.heappush(rows, (-mat[i].count(1), -i))
            if len(rows) > k:
                heapq.heappop(rows)
        
        rows.sort(key = lambda X: (-X[0], -X[1]))
        return [-idx for c, idx in rows]