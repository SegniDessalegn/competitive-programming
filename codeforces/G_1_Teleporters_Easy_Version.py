
for _ in range(int(input())):
    n, c = tuple(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(n):
        t[i] = (t[i], i + 1)
    t.sort(key = lambda X: (X[0] + X[1], X[1]))
    ans = 0
    for i in range(n):
        c -= t[i][1]
        if c < t[i][0]:
            break
        c -= t[i][0]
        ans += 1

    print(ans)