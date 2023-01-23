for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    valid = True
    for i in range(1, n):
        if arr[i] - arr[i - 1] > 1:
            valid = False
            break
    if valid:
        print("YES")
    else:
        print("NO")