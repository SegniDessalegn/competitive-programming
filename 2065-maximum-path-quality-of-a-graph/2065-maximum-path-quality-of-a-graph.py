class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        time = {}
        for edge in edges:
            a, b, t = edge
            graph[a].append(b)
            graph[b].append(a)
            time[(a, b)] = t
            time[(b, a)] = t
        
        
        def recur(node, currTime, added):
            nonlocal ans
            if currTime <= maxTime:
                if node == 0:
                    currSum = 0
                    for n in added:
                        currSum += values[n]
                    ans = max(ans, currSum)
            else:
                return
            
            for n in graph[node]:
                recur(n, currTime + time[(node, n)], added | set([n]))
        
        ans = 0
        recur(0, 0, set([0]))
        return ans
