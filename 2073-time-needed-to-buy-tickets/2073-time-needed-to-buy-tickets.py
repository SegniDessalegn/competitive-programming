class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        for i in range(len(tickets)):
            tickets[i] = [tickets[i], i]
        tickets = deque(tickets)
        time = 0
        
        while tickets:
            popped = tickets.popleft()
            time += 1
            popped[0] -= 1
            if popped[0] != 0:
                tickets.append(popped)
            elif popped[1] == k:
                break
        
        return time