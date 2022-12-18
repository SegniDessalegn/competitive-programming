class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        queue = deque([0])
        limit = jug1Capacity + jug2Capacity
        visited = set([0])
        while queue:
            curr = queue.popleft()
            if curr == targetCapacity:
                return True
            if curr > limit or curr < 0:
                continue
            if curr + jug1Capacity not in visited:
                queue.append(curr + jug1Capacity)
                visited.add(curr + jug1Capacity)
            if curr - jug1Capacity not in visited:
                queue.append(curr - jug1Capacity)
                visited.add(curr - jug1Capacity)
            if curr + jug2Capacity not in visited:
                queue.append(curr + jug2Capacity)
                visited.add(curr + jug2Capacity)
            if curr - jug2Capacity not in visited:
                queue.append(curr - jug2Capacity)
                visited.add(curr - jug2Capacity)
        return False