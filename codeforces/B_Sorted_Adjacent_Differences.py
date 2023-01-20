
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()

    i = n // 2
    if n % 2 == 0:
        i -= 1
    a1 = []
    for j in range(i + 1, n):
        a1.append(arr[j])
    a2 = []
    for j in range(i - 1, -1, -1):
        a2.append(arr[j])
    
    ans = [arr[i]]
    i = 0
    while i < (min(len(a1), len(a2))):
        ans.append(a1[i])
        ans.append(a2[i])
        i += 1
    
    while i < len(a1):
        ans.append(a1[i])
        i += 1
    while i < len(a2):
        ans.append(a2[i])
        i += 1
    
    print(*ans)