class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def traverse(node):
            nonlocal visited_count, visited
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    traverse(neighbour)
                visited_count[neighbour] += 1
        
        def valid(count):
            nodes = len(count)
            for node in count:
                if count[node] != nodes - 1:
                    return False
            return True
        
        visited = set()
        count = 0
        visited_count = defaultdict(int)
        for start in range(n):
            if start not in visited:
                visited.add(start)
                traverse(start)
                if valid(visited_count):
                    count += 1
                visited_count = defaultdict(int)
        
        return count
    