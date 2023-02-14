
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    once = False
    twice = False
    for i in range(1, n):
        if arr[i - 1] == arr[i] == -1:
            twice = True
        if arr[i - 1] == -1 or arr[i] == -1:
            once = True
    
    if twice:
        print(sum(arr) + 4)
    elif not once:
        print(sum(arr) - 4)
    else:
        print(sum(arr))