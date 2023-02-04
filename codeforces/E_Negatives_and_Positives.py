
for _ in range(int(input())):
    l = int(input())
    arr = list(map(int, input().split()))

    neg = 0
    large = -float("inf")
    for n in arr:
        if n < 0:
            neg += 1
        if n <= 0:
            large = max(large, n)

    ans = 0
    for i in range(l):
        ans += abs(arr[i])
    
    if neg % 2 != 0:
        arr.remove(large)
        small = abs(arr[0])
        for n in arr:
            small = min(small, abs(n))
        
        if abs(large) >= small:
            ans -= 2 * small
        else:
            ans += 2 * large
    
    print(ans)