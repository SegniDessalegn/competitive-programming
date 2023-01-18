n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)

l = 0
r = n - 1

while l < n:
    if arr[l] != sorted_arr[l]:
        break
    l += 1

while r > l:
    if arr[r] != sorted_arr[r]:
        break
    r -= 1

i = l
j = r
valid = True
while i < r:
    if arr[i] != sorted_arr[j]:
        valid = False
        break
    i += 1
    j -= 1

if valid:
    print("yes")
    if l == n:
        l = 0
        r = 0
    print(l + 1, r + 1)
else:
    print("no")