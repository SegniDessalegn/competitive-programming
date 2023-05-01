class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards = set(tuple(guard) for guard in guards)
        walls = set(tuple(wall) for wall in walls)
        not_guarded_count = (m * n) - len(guards) - len(walls)
        guarded = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if (i, j) in guards:
                    for dx, dy in directions:
                        r, c = i, j
                        while 0 <= r < m and 0 <= c < n and (r, c) not in walls:
                            if (r, c) != (i, j) and (r, c) in guards:
                                break
                            if (r, c) not in guarded and (r, c) not in guards:
                                not_guarded_count -= 1
                                guarded.add((r, c))
                            r, c = r + dx, c + dy
        return not_guarded_count