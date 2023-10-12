class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        ancestors = {i:set() for i in range(n)}
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            for neighbour in graph[curr]:
                in_degree[neighbour] -= 1
                ancestors[neighbour] = ancestors[neighbour].union(ancestors[curr])
                ancestors[neighbour].add(curr)
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        ans = []
        for i in range(n):
            ans.append(sorted(list(ancestors[i])))
        
        return ans