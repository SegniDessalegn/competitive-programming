class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        groups = [None for i in range(n)]
        graph = defaultdict(list)
        for edge in dislikes:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        for i in range(1, n + 1):
            if i not in visited:
                visited.add(i)
                queue = deque([(i, 1)])
                groups[i - 1] = 1
                while queue:
                    curr, curr_group = queue.popleft()
                    for n in graph[curr]:
                        if n not in visited:
                            groups[n - 1] = 1 if curr_group == 0 else 0
                            queue.append((n, groups[n - 1]))
                            visited.add(n)
                        elif not groups[n - 1] ^ curr_group:
                            return False
        return True
        