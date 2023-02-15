input()

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

p1 = 0
p2 = 0
ans = []
while p2 < len(arr2):
    while p1 < len(arr1) and arr1[p1] < arr2[p2]:
        p1 += 1
    ans.append(p1)
    p2 += 1

print(*ans)