
a, b = tuple(map(int, input().split()))

ops = []
while True:
    ops.append(b)
    if b == a:
        print("YES")
        print(len(ops))
        print(*ops[::-1])
        exit(0)
    elif b < a:
        break
    if b % 2 == 0:
        b //= 2
    else:
        if str(b)[-1] == "1":
            b = int(str(b)[:-1])
        else:
            break

print("NO")