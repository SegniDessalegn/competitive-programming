n = int(input())
 
arr = list(map(int, input().split()))
arr.sort()
if arr[-1] < arr[-2] + arr[0]:
    print("YES")
    print(*arr)
else:
    if arr[-1] < arr[-2] + arr[-3]:
        print("YES")
        arr[-1], arr[-2] = arr[-2], arr[-1]
    else:
        print("NO")