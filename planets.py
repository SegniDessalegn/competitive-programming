from collections import Counter


t = int(input())

for _ in range(t):
    n, c = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    count = Counter(arr)
    cost = 0
    for orbit in count:
        if count[orbit] == 1:
            cost += 1
        else:
            if count[orbit] <= c:
                cost += count[orbit]
            else:
                cost += c
    print(cost)