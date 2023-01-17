from collections import Counter, defaultdict


m, n = tuple(map(int, input().split()))

mat = []
for i in range(m):
    mat.append(input())

row_count = {}
for i in range(m):
    row_count[i] = Counter(mat[i])

col_count = {}
for j in range(n):
    curr_count = defaultdict(int)
    for i in range(m):
        curr_count[mat[i][j]] += 1
    col_count[j] = curr_count

decrypted = ""
for i in range(m):
    for j in range(n):
        curr = mat[i][j]
        if row_count[i][curr] == 1 and col_count[j][curr] == 1:
            decrypted += curr

print(decrypted)