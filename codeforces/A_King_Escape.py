
board_size = int(input())

a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))
x, y = tuple(map(int, input().split()))

if min(c, x) < a < max(c, x) or min(d, y) < b < max(d, y):
    print("NO")
else:
    print("YES")