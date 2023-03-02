
for _ in range(int(input())):
    n = int(input())
    s = list(input().lower())
    p = 0
    count = 0
    while p < n and s[p] == "m":
        if count == 0:
            count += 1
        p += 1
    if count == 0:
        print("NO")
        continue
    
    while p < n and s[p] == "e":
        if count == 1:
            count += 1
        p += 1
    if count == 1:
        print("NO")
        continue
    while p < n and s[p] == "o":
        if count == 2:
            count += 1
        p += 1
    if count == 2:
        print("NO")
        continue
    
    while p < n and s[p] == "w":
        if count == 3:
            count += 1
        p += 1
    if count == 3:
        print("NO")
        continue

    if p >= n:
        print("YES")
    else:
        print("NO")