
for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))
    s = input()
    ans = 0
    lower = [0] * 26
    upper = [0] * 26

    for char in s:
        if char.isupper():
            upper[ord(char) - 65] += 1
        else:
            lower[ord(char) - 97] += 1
    
    for i in range(26):
        diff = min(lower[i], upper[i])
        lower[i] -= diff
        upper[i] -= diff
        ans += diff
        if k > 0:
            diff = (max(lower[i], upper[i]) - min(lower[i], upper[i])) // 2
            if diff <= k:
                k -= diff
                ans += diff
            else:
                ans += k
                k = 0
        
    print(ans)
