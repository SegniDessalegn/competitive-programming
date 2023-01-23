for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    left = 0
    right = 1
    count = 0
    while right < n:
        if arr[right - 1] < 2 * arr[right]:
            if right - left >= k:
                count += 1
                left += 1
        else:
            left = right
        right += 1
    
    print(count)