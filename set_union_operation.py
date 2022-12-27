input()
set1 = set(map(int, input().split()))
input()
set2 = set(map(int, input().split()))

for s in set2:
    set1.add(s)

print(len(set1))