class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        degree_count = defaultdict(int)
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            degree_count[u] += 1
            degree_count[v] += 1
        
        queue = deque()
        visited = set()
        for num in degree_count:
            if degree_count[num] == 1:
                queue.append(num)
                visited.add(num)
                break
        
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        
        return ans
    