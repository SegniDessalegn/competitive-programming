
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    arr = []
    for i in range(n):
        arr.append((b[i], i))
    
    arr.sort()

    min_index = [arr[-1][1]]
    for i in range(n):
        if arr[-i - 1][1] < min_index[-1]:
            min_index.append(arr[-i - 1][1])
        else:
            min_index.append(min_index[-1])
    min_index = min_index[::-1]
    
    ans = float("inf")
    for i in range(n):
        left = 0
        right = n - 1
        while left <= right:
            index = (left + right) // 2
            if arr[index][0] > a[i]:
                right = index - 1
            else:
                left = index + 1
        ans = min(ans, i + min_index[left])
    
    print(ans)
    