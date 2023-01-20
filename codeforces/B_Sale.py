n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

arr.sort()
ans = 0
for i in range(m):
    if arr[i] >= 0:
        break
    ans += (-arr[i])

print(ans)