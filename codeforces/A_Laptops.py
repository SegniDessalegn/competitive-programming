n = int(input())

arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
    
arr.sort()
r = arr[0][1]
for i in range(n):
    if arr[i][1] < r:
        print("Happy Alex")
        exit(0)
    if arr[i][1] > r:
        r = arr[i][1]

print("Poor Alex")