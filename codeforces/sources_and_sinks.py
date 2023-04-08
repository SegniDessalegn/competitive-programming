
n = int(input())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

sources = []
sinks = []

for j in range(n):
    valid = True
    for i in range(n):
        if mat[i][j] == 1:
            valid = False
            break
    if valid:
        sources.append(j + 1)

for i in range(n):
    valid = True
    for j in range(n):
        if mat[i][j] == 1:
            valid = False
            break
    if valid:
        sinks.append(i + 1)

print(len(sources), *sources)
print(len(sinks), *sinks)
