class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])
        unvisited = set([i for i in range(len(rooms))])
        while queue:
            curr = queue.popleft()
            unvisited.discard(curr)
            for key in rooms[curr]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        
        return True if not unvisited else False