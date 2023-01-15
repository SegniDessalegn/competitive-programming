N = int(input())

for _ in range(N):
    n, m = tuple(map(int, input().split()))
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    
    pref_sum1 = {}
    for start in range(n):
        i, j = start, 0
        curr_sum = 0
        while 0 <= i < n and 0 <= j < m:
            curr_sum += mat[i][j]
            i += 1
            j += 1
        pref_sum1[start] = curr_sum
    
    for start in range(m):
        i, j = 0, start
        curr_sum = 0
        while 0 <= i < n and 0 <= j < m:
            curr_sum += mat[i][j]
            i += 1
            j += 1
        pref_sum1[-start] = curr_sum
    
    pref_sum2 = {}
    for start in range(m):
        i, j = 0, start
        curr_sum = 0
        while 0 <= i < n and 0 <= j < m:
            curr_sum += mat[i][j]
            i += 1
            j -= 1
        pref_sum2[start] = curr_sum
    
    for start in range(n):
        i, j = start, m - 1
        curr_sum = 0
        while 0 <= i < n and 0 <= j < m:
            curr_sum += mat[i][j]
            i += 1
            j -= 1
        pref_sum2[start + m - 1] = curr_sum
    
    max_sum = 0
    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum, pref_sum1[i - j] + pref_sum2[i + j] - mat[i][j])
    
    print(max_sum)