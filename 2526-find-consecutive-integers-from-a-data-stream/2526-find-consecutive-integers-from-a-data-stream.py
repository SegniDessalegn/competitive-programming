class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.count = {}

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.count[num] = self.count.get(num, 0) + 1
        if len(self.queue) > self.k:
            popped = self.queue.popleft()
            self.count[popped] -= 1
            if self.count[popped] == 0:
                self.count.pop(popped)
        
        return num == self.value and self.count[num] == self.k
