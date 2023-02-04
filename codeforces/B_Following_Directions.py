
for _ in range(int(input())):
    input()
    op = input()
    x, y = 0, 0
    valid = False
    for o in op:
        if o == "U":
            y += 1
        if o == "D":
            y -= 1
        if o == "R":
            x += 1
        if o == "L":
            x -= 1
        
        if (x, y) == (1, 1):
            valid = True
            break
    
    if valid:
        print("YES")
    else:
        print("NO")