
vertexes = int(input())
operations = int(input())

graph = {i + 1:[] for i in range(vertexes)}
for _ in range(operations):
    curr = tuple(map(int, input().split()))
    if curr[0] == 1:
        graph[curr[1]].append(curr[2])
        graph[curr[2]].append(curr[1])
    else:
        print(*graph[curr[1]])