
vertexes = int(input())
operations = int(input())

graph = {i + 1:set() for i in range(vertexes)}
for _ in range(operations):
    curr = tuple(map(int, input().split()))
    if curr[0] == 1:
        graph[curr[1]].add(curr[2])
        graph[curr[2]].add(curr[1])
    else:
        if graph[curr[1]]:
            print(*graph[curr[1]])
        else:
            print()