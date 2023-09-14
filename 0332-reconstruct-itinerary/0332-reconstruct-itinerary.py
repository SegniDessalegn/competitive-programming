class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's algorithm to find Eulerian path
        
        graph = defaultdict(set)
        edges = defaultdict(int)
        for u, v in tickets:
            graph[u].add(v)
            edges[(u, v)] += 1
        
        for n in graph:
            graph[n] = sorted(list(graph[n]))
        
        
        def dfs(node):
            nonlocal ans
            
            for neighbour in graph[node]:
                if edges[(node, neighbour)] != 0:
                    edges[(node, neighbour)] -= 1
                    dfs(neighbour)
            ans.append(node)
        
        ans = []
        dfs("JFK")
        
        return ans[::-1]