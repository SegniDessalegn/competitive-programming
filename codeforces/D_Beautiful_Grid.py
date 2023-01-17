
def generate(i, j, n):
    rotated = set()
    rotated.add((i, j))
    rotated.add((j, n - i - 1))
    rotated.add((n - i - 1, n - j - 1))
    rotated.add((n - j - 1, i))
    
    return rotated

for _ in range(int(input())):
    mat = []
    n = int(input())
    for _ in range(n):
        mat.append(input())
    
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            zero_count = 0
            one_count = 0
            for rot in generate(i, j, n):
                if mat[rot[0]][rot[1]] == "0":
                    zero_count += 15
                else:
                    one_count += 1
            
            count += min(zero_count, one_count)
    
    print(count // 4)