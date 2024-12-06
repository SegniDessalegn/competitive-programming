class UndergroundSystem:
    
    def __init__(self):
        self.checkedIn = {}
        self.completed = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prev = self.checkedIn[id]
        key = (prev[0], stationName)
        self.completed[key][0] += t - prev[1]
        self.completed[key][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.completed[key][0] / self.completed[key][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)