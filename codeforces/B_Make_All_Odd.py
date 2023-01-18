
for _ in range(int(input())):
    l = int(input())
    arr = list(map(int, input().split()))
    even_count = 0
    for n in arr:
        if n % 2 == 0:
            even_count += 1
    
    if even_count < l:
        print(even_count)
    else:
        print("-1")