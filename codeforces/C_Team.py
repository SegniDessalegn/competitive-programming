
for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))

    arr = list(map(int, input().split()))

    arr.sort()
    
    left = 0
    right = n - 1
    teams = 0
    while left <= right:
        if arr[right] >= k:
            teams += 1
            right -= 1
        elif left != right and arr[right] + arr[left] >= k:
            teams += 1
            right -= 1
            left += 1
        else:
            left += 1
    
    print(teams)