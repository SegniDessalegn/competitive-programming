from collections import Counter

k = int(input())
counts =  Counter(list(map(int,input().split())))

for n in counts:
    if counts[n] == 1:
        print(n)
