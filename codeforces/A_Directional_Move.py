
from collections import deque


for _ in range(int(input())):
    l = int(input())
    arr = []
    for char in input():
        arr.append(char)
    
    queue = deque(["E", "S", "W", "N"])
    
    for i in range(l):
        if arr[i] == "0":
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())
    
    print(queue[0])