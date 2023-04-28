class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set([(0, 1)])
        while queue:
            pos, speed, instructions = queue.popleft()
            if pos == target:
                return instructions
            if (pos + speed, speed * 2) not in visited:
                visited.add((pos + speed, speed * 2))
                queue.append((pos + speed, speed * 2, instructions + 1))
            if speed > 0:
                if (pos, -1) not in visited:
                    visited.add((pos, -1))
                    queue.append((pos, -1, instructions + 1))
            else:
                if (pos, 1) not in visited:
                    visited.add((pos, 1))
                    queue.append((pos, 1, instructions + 1))
        
        return -1