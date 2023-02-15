n = int(input())

arr = list(map(int, input().split()))

arr.sort()

if sum(arr[:n]) == sum(arr[n:]):
    print(-1)
else:
    print(*arr)