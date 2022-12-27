input()
set1 = set(map(int, input().split()))
input()
set2 = set(map(int, input().split()))

count = 0
for s in set1:
    if s not in set2:
        count += 1
print(count)