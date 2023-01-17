n, k = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

arr.sort()

num = -1
if k == 0 and arr[0] > 1:
    num = arr[0] - 1
elif n == k:
    num = arr[-1]
elif 0 < k < n and arr[k - 1] != arr[k]:
    num = arr[k - 1]

print(num)