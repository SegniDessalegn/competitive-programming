
for _ in range(int(input())):
    n = int(input())
    s = input()
    l = 0
    r = n - 1
    ans = n
    while l < r and s[l] != s[r]:
        l += 1
        r -= 1
        ans = min(ans, r - l + 1)

    print(ans)