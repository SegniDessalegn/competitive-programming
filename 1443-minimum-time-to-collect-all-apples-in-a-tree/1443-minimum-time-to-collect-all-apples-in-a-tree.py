class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        def calculate_time(node, visited):
            time = 0
            path = False
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    n_time, n_path = calculate_time(n, visited)
                    if hasApple[n] or n_path:
                        time += 2 + n_time
                    path = path or hasApple[n] or n_path
                    visited.add(n)
            return (time, path)
        
        graph = {i:[] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return calculate_time(0, set([0]))[0]