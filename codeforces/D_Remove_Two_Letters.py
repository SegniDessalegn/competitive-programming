
for _ in range(int(input())):
    n = int(input())
    arr = input()
    count = 1
    for i in range(1, n - 1):
        if arr[i - 1] != arr[i + 1]:
            count += 1
    print(count)