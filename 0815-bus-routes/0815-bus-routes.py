class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stations = defaultdict(list)
        for i in range(len(routes)):
            routes[i] = set(routes[i])
            for station in routes[i]:
                stations[station].append(i)
        
        queue = deque()
        visited = set()
        for bus in stations[source]:
            queue.append((bus, 1))
            visited.add(bus)
        
        while queue:
            curr, dist = queue.popleft()
            if target in routes[curr]:
                return dist
            for station in routes[curr]:
                for bus in stations[station]:
                    if bus not in visited:
                        visited.add(bus)
                        queue.append((bus , dist + 1))
        
        return -1