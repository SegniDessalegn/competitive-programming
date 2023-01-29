
for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))

    ans = []
    l = 0
    r = n - 1
    t = True
    while l <= r:
        if t:
            ans.append(seq[l])
            l += 1
        else:
            ans.append(seq[r])
            r -= 1
        t = not t
    
    print(*ans)