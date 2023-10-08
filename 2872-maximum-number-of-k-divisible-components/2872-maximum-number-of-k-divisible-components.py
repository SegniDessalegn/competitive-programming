class Solution:
    def maxKDivisibleComponents(self, N: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        total = [values[i] for i in range(N)]
        
        # calculate the sum
        def calculate(node, parent):
            
            curr_sum = values[node]
            for neighbour in graph[node]:
                if neighbour != parent:
                    curr_sum += calculate(neighbour, node)
            
            total[node] = curr_sum
            return curr_sum
        
        calculate(0, -1)
        
        count = 0
        for node in range(N):
            if total[node] % k == 0:
                count += 1
        
        return count