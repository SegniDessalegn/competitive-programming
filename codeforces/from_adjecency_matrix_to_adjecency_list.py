
n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

graph = {i + 1:[] for i in range(n)}
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            graph[i + 1].append(j + 1)

for i in range(n):
    print(len(graph[i + 1]), *graph[i + 1])
