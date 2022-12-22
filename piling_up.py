T = int(input())
for i in range(T):
    input()
    l = list(map(int, input().split()))

    i, j = 0, len(l) - 1
    curr = float("inf")
    ans = True
    while i <= j:
        if l[i] >= l[j]:
            if l[i] <= curr:
                curr = l[i]
                i += 1
            else:
                ans = False
                break
        else:
            if l[j] <= curr:
                curr = l[j]
                j -= 1
            else:
                ans = False
                break
            
    if ans:
        print("Yes")
    else:
        print("No")
