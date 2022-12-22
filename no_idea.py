l = input()
arr = list(map(int, input().split()))

A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

happiness = 0
for n in arr:
    if n in A:
        happiness += 1
    elif n in B:
        happiness -= 1

print(happiness)
