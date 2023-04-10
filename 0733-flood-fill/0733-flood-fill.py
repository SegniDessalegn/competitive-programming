class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        initial_color = image[sr][sc]
        if initial_color == color:
            return image
        image[sr][sc] = color
        queue = deque([(sr, sc)])
        while queue:
            x, y = queue.popleft()
            for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if  0 <= r < m and 0 <= c < n and image[r][c] == initial_color:
                    image[r][c] = color
                    queue.append((r,c))
        return image