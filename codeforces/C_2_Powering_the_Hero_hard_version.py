 
import heapq
 
 
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
 
    score = 0
    heap = []
    for i in range(n):
        if arr[i] != 0:
            heapq.heappush(heap, -arr[i])
        else:
            if heap:
                score += -heapq.heappop(heap)
    
    print(score)