
from collections import Counter


for _ in range(int(input())):
    n, m, k = tuple(map(int, input().split()))
    a = list(input())
    b = list(input())

    a.sort(reverse = True)
    b.sort(reverse = True)

    a_count = Counter(a)
    b_count = Counter(b)
    ac = 0
    bc = 0
    c = ""
    while a and b:
        if bc >= k or (ac < k and a[-1] < b[-1]):
            c += a[-1]
            a_count[a[-1]] -= 1
            a.pop()
            ac += 1
            bc = 0
        elif a[-1] > b[-1]:
            c += b[-1]
            b_count[b[-1]] -= 1
            b.pop()
            bc += 1
            ac = 0
        else:
            if bc >= k or (ac < k and a_count[a[-1]] > b_count[b[-1]]):
                c += a[-1]
                a_count[a[-1]] -= 1
                a.pop()
                ac += 1
                bc = 0
            else:
                c += b[-1]
                b_count[b[-1]] -= 1
                b.pop()
                bc += 1
                ac = 0
    
    print(c)