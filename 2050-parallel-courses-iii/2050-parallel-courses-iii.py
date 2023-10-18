class Solution:
    def minimumTime(self, N: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = defaultdict(list)
        in_degree = {course:0 for course in range(N)}
        for u, v in relations:
            graph[u - 1].append(v - 1)
            in_degree[v - 1] += 1
        
        queue = deque()
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)
        
        total_time = [0 for _ in range(N)]
        while queue:
            curr_course = queue.popleft()
            total_time[curr_course] += time[curr_course]
            for neighbour in graph[curr_course]:
                total_time[neighbour] = max(total_time[neighbour], total_time[curr_course])
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        return max(total_time)