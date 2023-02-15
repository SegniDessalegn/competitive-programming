m = int(input())
a = list(map(int, input().split()))
n = int(input())
b = list(map(int, input().split()))

a.sort()
b.sort()

p1 = 0
p2 = 0

count = 0

while p1 < m and p2 < n:
    valid = True
    while p1 < m and p2 < n and abs(a[p1] - b[p2]) > 1:
        if a[p1] < b[p2]:
            p1 += 1
        else:
            p2 += 1
        if p1 >= m or p2 >= n:
            valid = False
    if valid:
        count += 1
    p1 += 1
    p2 += 1

print(count)