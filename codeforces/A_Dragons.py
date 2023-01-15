strength, n = tuple(map(int, input().split()))

arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda X: (X[0], -X[1]))

valid = True
for i in range(len(arr)):
    if strength <= arr[i][0]:
        valid = False
        break
    strength += arr[i][1]

if valid:
    print("YES")
else:
    print("NO")