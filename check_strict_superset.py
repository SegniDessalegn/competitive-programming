A = set(map(int, input().split(" ")))
n = int(input())
N = []

for i in range(n):
    N.append(set(map(int, input().split(" "))))

for s in N:
    superset = True
    if len(A) <= len(s):
        print("False")
        break
    for i in s:
        if i not in A:
            superset = False
            break
    if not superset:
        print("False")
        break

if superset:
    print("True")
