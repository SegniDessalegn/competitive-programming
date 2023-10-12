import math
 
 
n, m = list(map(int, input().split()))
 
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
 
dist = [math.inf] * (n + 1)
parent = [-1 for _ in range(n + 1)]
 
for _ in range(n - 1):
    for u, v, w in edges:
        if dist[u] == math.inf:
            dist[u] = 0
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
 
for u, v, w in edges:
    if dist[u] == math.inf:
        dist[u] = 0
        parent[v] = u
    if dist[u] + w < dist[v]:
        node = v
        index = 0
        index_map = {}
        stack = []
        while True:
            stack.append(node)
            if node in index_map:
                idx = index_map[node]
                print("YES")
                print(*stack[idx:][::-1])
                break
            index_map[node] = index
            index += 1
            node = parent[node]
        exit(0)
 
print("NO")
