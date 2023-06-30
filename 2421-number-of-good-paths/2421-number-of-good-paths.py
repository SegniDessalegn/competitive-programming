class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        def find(x):
            nodes = []
            while x != reps[x]:
                nodes.append(x)
                x = reps[x]
            for n in nodes:
                reps[n] = x
            return x
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            reps[y_rep] = x_rep
        
        
        N = len(vals)
        reps = {i:i for i in range(N)}
        val_nodes = defaultdict(list)
        for node in range(N):
            val_nodes[vals[node]].append(node)
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = N
        for val in sorted(val_nodes.keys()):
            for node in val_nodes[val]:
                for neighbour in graph[node]:
                    if val >= vals[neighbour]:
                        union(node, neighbour)
            
            prev = Counter()
            for node in val_nodes[val]:
                ans += prev[find(node)]
                prev[find(node)] += 1
        
        return ans