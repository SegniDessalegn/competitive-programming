n = int(input())

arr = list(map(int, input().split()))

arr.sort()
count = 0
for i in range(1, n, 2):
    count += (arr[i] - arr[i - 1])

print(count)