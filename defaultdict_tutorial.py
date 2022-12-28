from collections import defaultdict 

n, m = map(int, input().split())

A = defaultdict(list)
for i in range(n):
    A[input()].append(i + 1)

for j in range(m):
    arr = A[input()]
    if not arr:
        print(-1, end = "")
    for char in arr:
        print(char, end = " ")
    print()