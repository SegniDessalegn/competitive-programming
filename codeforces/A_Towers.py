from collections import defaultdict

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

height = defaultdict(lambda:1)
dist = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        height[arr[i]] += 1
    else:
        dist += 1

max_height = 1
for n in height.values():
    max_height = max(max_height, n)

print(max_height, dist)