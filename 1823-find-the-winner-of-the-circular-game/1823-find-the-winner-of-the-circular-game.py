class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([i + 1 for i in range(n)])
        while len(queue) != 1:
            for _ in range(k - 1):
                queue.append(queue.popleft())
            queue.popleft()
        
        return queue[0]