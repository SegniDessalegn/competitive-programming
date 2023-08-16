class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        xor = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        heap = []
        for i in range(1, m + 1):
            row_xor = 0
            for j in range(1, n + 1):
                xor[i][j] = xor[i - 1][j] ^ row_xor ^ matrix[i - 1][j - 1]
                row_xor ^= matrix[i - 1][j - 1]
                
                heapq.heappush(heap, xor[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return min(heap)