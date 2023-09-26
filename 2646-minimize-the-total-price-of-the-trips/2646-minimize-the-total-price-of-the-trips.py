class Solution:
    def minimumTotalPrice(self, N: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        # first calculate how much each node gets visited
        # do dp on the calculated cost
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited_count = [0] * N
        
        def calculate(start, end):
            
            queue = deque([start])
            visited = set([start])
            parent = [-1] * N
            while queue:
                
                curr = queue.popleft()
                
                if curr == end:
                    break
                
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
                        parent[neighbour] = curr
            
            # path reconstruction
            current = end
            while parent[current] != -1:
                visited_count[current] += 1
                current = parent[current]
            
            visited_count[start] += 1
        
        
        @cache
        def find_ans(node, parent, parent_half):
            curr = float("inf")
            if not parent_half:
                current_cost = visited_count[node] * (price[node] // 2)
                for neighbour in graph[node]:
                    if neighbour != parent:
                        current_cost += find_ans(neighbour, node, True)
                
                curr = min(curr, current_cost)
            
            current_cost = visited_count[node] * price[node]
            for neighbour in graph[node]:
                if neighbour != parent:
                    current_cost += find_ans(neighbour, node, False)
            
            curr = min(curr, current_cost)
            
            return curr
        
        for s, e in trips:
            calculate(s, e)
        
        return find_ans(0, -1, False)