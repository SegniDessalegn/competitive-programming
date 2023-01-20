n = int(input())

arr = list(map(int, input().split()))

arr.sort()
left = 0
right = n - 1
ans = []
l = True
while left <= right:
    if l:
        ans.append(arr[left])
        left += 1
    else:
        ans.append(arr[right])
        right -= 1
    l = not l

print(*ans)