
for _ in range(int(input())):
    a, b = tuple(map(int, input().split()))
    print(min(a, b, (a + b) // 4))