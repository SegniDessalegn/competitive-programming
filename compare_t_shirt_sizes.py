
def compare(s1, s2):
    if len(s1) > len(s2):
        print(">")
    elif len(s1) < len(s2):
        print("<")
    else:
        print("=")

N = int(input())

for i in range(N):
    s1, s2 = tuple(map(str, input().split()))
    if s1[-1] == "L":
        if s2[-1] == "L":
            compare(s1, s2)
        else:
            print(">")
    elif s1[-1] == "M":
        if s2[-1] == "L":
            print("<")
        elif s2[-1] == "M":
            compare(s1, s2)
        else:
            print(">")
    elif s1[-1] == "S":
        if s2[-1] == "S":
            compare(s2, s1)
        else:
            print("<")

