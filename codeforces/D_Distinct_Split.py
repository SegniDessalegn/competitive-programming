
from collections import Counter


for _ in range(int(input())):
    n = int(input())
    s = input()
    right = Counter(s)
    left = {}
    curr = len(right)
    ans = 0
    for char in s:
        right[char] -= 1
        left[char] = left.get(char, 0) + 1
        if left[char] == 1:
            curr += 1
        if right[char] == 0:
            curr -= 1
        ans = max(ans, curr)
    
    print(ans)