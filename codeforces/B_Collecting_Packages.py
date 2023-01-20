for _ in range(int(input())):
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(tuple(map(int, input().split())))
    
    arr.sort()
    valid = True
    path = ("R" * arr[0][0]) + ("U" * arr[0][1])
    for i in range(1, n):
        if arr[i][1] - arr[i - 1][1] < 0:
            valid = False
            break
        path += ("R" * (arr[i][0] - arr[i - 1][0])) + ("U" * (arr[i][1] - arr[i - 1][1]))
    
    if valid:
        print("YES")
        print(path)
    else:
        print("NO")