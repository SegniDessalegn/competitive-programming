n, k = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

count = 0
for n in arr:
    if n >= arr[k - 1] and n > 0:
        count += 1

print(count)