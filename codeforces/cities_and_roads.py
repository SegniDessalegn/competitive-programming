
n = int(input())
roads = 0
for i in range(n):
    roads += input().split()[i:].count("1")

print(roads)