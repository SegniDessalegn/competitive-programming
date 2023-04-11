class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = {i:[] for i in range(len(bombs))}
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if self.distance(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]) <= bombs[i][2]:
                    graph[i].append(j)
            
        max_count = 0
        for g in graph:
            curr_count = 1
            visited = set([g])
            queue = deque([g])
            while queue:
                curr = queue.popleft()
                for n in graph[curr]:
                    if n not in visited:
                        curr_count += 1
                        queue.append(n)
                        visited.add(n)
            max_count = max(max_count, curr_count)
        
        return max_count
    
    
    def distance(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)