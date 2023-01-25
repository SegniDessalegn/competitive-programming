n = int(input())
arr = list(map(int, input().split()))
odd = 0
even = 0
for n in arr:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

if odd == 0 or even == 0:
    print(*arr)
else:
    arr.sort()
    print(*arr)