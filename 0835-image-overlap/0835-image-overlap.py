class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # brute-force, BFS
        
        def get_overlap(x_offset, y_offset):
            count = 0
            for i in range(N):
                for j in range(N):
                    x_real = i + x_offset
                    y_real = j + y_offset
                    if 0 <= x_real < N and 0 <= y_real < N and img1[x_real][y_real] == img2[i][j] == 1:
                        count += 1
            return count
        
        N = len(img1)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        ans = 0
        while queue:
            x_offset, y_offset = queue.popleft()
            ans = max(ans, get_overlap(x_offset, y_offset))
            for dx, dy in directions:
                new_x_offset, new_y_offset = x_offset + dx, y_offset + dy
                if -N < new_x_offset < N and -N < new_y_offset < N and (new_x_offset, new_y_offset) not in visited:
                    queue.append((new_x_offset, new_y_offset))
                    visited.add((new_x_offset, new_y_offset))
        
        return ans