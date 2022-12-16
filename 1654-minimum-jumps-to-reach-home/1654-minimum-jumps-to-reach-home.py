class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited = set([0])
        queue = deque([(0, 0, True)])
        limit = max(x + a + b, max(list(forbidden)) + a + b)
        forbidden = set(forbidden)
        while queue:
            curr, d, back = queue.popleft()
            if curr > limit:
                continue
            if curr == x:
                return d
            if (curr + a, True) not in visited and curr + a not in forbidden:
                queue.append((curr + a, d + 1, True))
                visited.add((curr + a, True))
            if back and curr - b > 0 and (curr - b, False) not in visited and curr - b not in forbidden:
                queue.append((curr - b, d + 1, False))
                visited.add((curr - b, False))
        return -1
            