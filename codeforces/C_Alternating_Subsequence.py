def changed_sign(m, n):
    return (m > 0 and n < 0) or (m < 0 and n > 0)

for _ in range(int(input())):
    l = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    curr_max = arr[0]
    for i in range(l):
        if i > 0 and changed_sign(arr[i - 1], arr[i]):
            max_sum += curr_max
            curr_max = arr[i]
        curr_max = max(curr_max, arr[i])
    max_sum += curr_max
    
    print(max_sum)