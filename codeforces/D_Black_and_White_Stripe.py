for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))
    s = input()
    i = 0
    j = 0
    flips = 0
    ans = n
    while j < n:
        if s[j] == "W":
            flips += 1
        if j - i + 1 == k:
            ans = min(ans, flips)
            if s[i] == "W":
                flips -= 1
            i += 1
        j += 1
    
    print(ans)
