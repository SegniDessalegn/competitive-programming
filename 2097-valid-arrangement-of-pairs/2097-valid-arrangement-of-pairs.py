class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for u, v in pairs:
            degree[u] += 1
            degree[v] -= 1
            graph[u].append(v)
        
        for node in graph:
            graph[node].sort()
        
        # if there is a node with odd degree, we have start from here, (or end here)
        start = None
        for node in degree:
            if degree[node] == 1:
                start = node
        
        if start is None:
            start = pairs[0][0]
        
        def dfs(node):
            nonlocal ans
            while graph[node]:
                dfs(graph[node].pop())
            ans.append(node)
            
        ans = []
        dfs(start)
        ans = ans[::-1]
        return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]