class MyCalendar:

    def __init__(self):
        self.saved = set()

    def book(self, startTime: int, endTime: int) -> bool:
        for a, b in self.saved:
            if a < endTime and b > startTime:
                return False
        self.saved.add((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)