m, n  = tuple(map(int, input().split()))

mat = []
for i in range(m):
    curr = []
    for c in input():
        curr.append(c)
    mat.append(curr)

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]    

s = False
for i in range(m):
    for j in range(n):
        if mat[i][j] == "S" and not s:
            for d in directions:
                pos = [i, j]
                while 0 <= pos[0] < m and 0 <= pos[1] < n:
                    if mat[pos[0]][pos[1]] == "*":
                        break
                    if mat[pos[0]][pos[1]] == "T":
                        print("YES")
                        exit(0)
                    mat[pos[0]][pos[1]] = "S"
                    pos[0] += d[0]
                    pos[1] += d[1]
            s = True

t = False
for i in range(m):
    for j in range(n):
        if mat[i][j] == "T" and not t:
            for d in directions:
                pos = [i, j]
                while 0 <= pos[0] < m and 0 <= pos[1] < n:
                    if mat[pos[0]][pos[1]] == "*":
                        break
                    if mat[pos[0]][pos[1]] == "S":
                        print("YES")
                        exit(0)
                    mat[pos[0]][pos[1]] = "T"
                    pos[0] += d[0]
                    pos[1] += d[1]
            t = True

for i in range(m):
    for j in range(n):
        if mat[i][j] == "S" or mat[i][j] == "T":
            curr = mat[i][j]
            for d in directions:
                pos = [i, j]
                while 0 <= pos[0] < m and 0 <= pos[1] < n:
                    if mat[pos[0]][pos[1]] == "*":
                        break
                    if mat[pos[0]][pos[1]] != "." and mat[pos[0]][pos[1]] != curr:
                        print("YES")
                        exit(0)
                    pos[0] += d[0]
                    pos[1] += d[1]

print("NO")