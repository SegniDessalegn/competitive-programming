class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        for i in range(N):
            costs[i] = (costs[i], i)
        
        ans = 0
        left = []
        right = []
        costs = deque(costs)
        
        for _ in range(candidates):
            if not costs:
                break
            heapq.heappush(left, costs.popleft())
            if not costs:
                break
            heapq.heappush(right, costs.pop())
        
        while k > 0:
            if left and not right:
                ans += heapq.heappop(left)[0]
            elif right and not left:
                ans += heapq.heappop(right)[0]
            elif left[0][0] <= right[0][0]:
                ans += heapq.heappop(left)[0]
                if costs:
                    heapq.heappush(left, costs.popleft())
            else:
                ans += heapq.heappop(right)[0]
                if costs:
                    heapq.heappush(right, costs.pop())
            k -= 1
            
        return ans