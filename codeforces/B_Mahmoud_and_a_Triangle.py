l = int(input())

arr = list(map(int, input().split()))

arr.sort()
valid = False
for i in range(2, len(arr)):
    if arr[i] < arr[i - 1] + arr[i - 2]:
        valid = True
        break

if valid:
    print("YES")
else:
    print("NO")