class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for u, v in edges:
            if u == v or u in graph[v]:
                return -1
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque()
        for i in range(len(colors)):
            if in_degree[i] == 0:
                queue.append(i)
        
        if not queue:
            return -1
        
        count = defaultdict(lambda: defaultdict(int))
        while queue:
            curr = queue.popleft()
            count[curr][colors[curr]] += 1
            
            for neighbour in graph[curr]:
                in_degree[neighbour] -= 1
                for c in count[curr]:
                    count[neighbour][c] = max(count[neighbour][c], count[curr][c])
                
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        if queue:
            return -1
        
        result = 0
        for node in range(len(colors)):
            for c in count[node]:
                result = max(result, count[node][c])
        
        return result
    