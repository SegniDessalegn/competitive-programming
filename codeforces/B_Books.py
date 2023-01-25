n, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

l = 0
r = 0
max_ans = 0
curr_time = 0
while r < n:
    curr_time += arr[r]
    while curr_time > t:
        curr_time -= arr[l]
        l += 1
    max_ans = max(max_ans, r - l + 1)
    r += 1

print(max_ans)