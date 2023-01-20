n, k, x = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

arr.sort()
groups = 1
d = []
for i in range(1, n):
    if arr[i] - arr[i - 1] > x:
        d.append((arr[i] - arr[i - 1] - 1) // x)
        groups += 1

d.sort()
l = len(d)
i = 0
while i < l:
    if k >= d[i]:
        k -= d[i]
        groups -= 1
    i += 1

print(groups)