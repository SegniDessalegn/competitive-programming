n, l = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

arr.sort()

d = 0
for i in range(1, n):
    d = max(d, arr[i] - arr[i - 1])

d /= 2
print(max(arr[0], l - arr[-1], d))