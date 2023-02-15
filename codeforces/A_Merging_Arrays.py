
n, m = tuple(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
p1 = 0
p2 = 0
merged = []
for i in range(n + m):
    if p2 >= m or (p1 < n and arr1[p1] < arr2[p2]):
        merged.append(arr1[p1])
        p1 += 1
    else:
        merged.append(arr2[p2])
        p2 += 1

print(*merged)