
for _ in range(int(input())):
    n = int(input())
    i = 0
    m = n
    valid = False
    while n >> 1:
        if n & 1:
            valid = True
            break
        i += 1
        n >>= 1
    
    ans = 2 ** i
    
    if not valid:
        i = 0
        while m:
            if not m & 1:
                break
            i += 1
            m >>= 1
        
        ans += 2 ** i
    
    print(ans)