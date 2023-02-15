from collections import Counter


m, n = tuple(map(int, input().split()))

arr = list(map(int, input().split()))
toys = []
for _ in range(n):
    toys.append(input())

arr.sort()

t_count = Counter(toys)
a_count = Counter(arr)

c = []
for t in t_count:
    c.append((t_count[t], t))

c.sort(reverse=True)
min = 0

p1 = 0
p2 = 0
while p1 < m and p2 < len(c):
    min += arr[p1] * c[p2][0]
    p2 += 1
    p1 += 1

max = 0
p1 = 0
p2 = 0
arr.sort(reverse=True)
while p1 < m and p2 < len(c):
    max += arr[p1] * c[p2][0]
    p2 += 1
    p1 += 1

print(min, max)