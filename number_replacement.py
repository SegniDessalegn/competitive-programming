N = int(input())

for i in range(N):
    input()
    arr = list(map(int, input().split()))
    chars = input()
    maps = {}
    is_rep = True
    for j in range(len(arr)):
        if arr[j] not in maps:
            maps[arr[j]] = chars[j]
        elif maps[arr[j]] != chars[j]:
            is_rep = False
            break
    if is_rep:
        print("Yes")
    else:
        print("No")
    