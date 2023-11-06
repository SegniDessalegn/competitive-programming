class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [i + 1 for i in range(n)]
        heapq.heapify(self.unreserved)
        self.reserved = set()

    def reserve(self) -> int:
        while self.unreserved[0] in self.reserved:
            heapq.heappop(self.unreserved)
        seat = heapq.heappop(self.unreserved)
        self.reserved.add(seat)
        return seat
        
    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self.reserved:
            heapq.heappush(self.unreserved, seatNumber)
            self.reserved.remove(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)