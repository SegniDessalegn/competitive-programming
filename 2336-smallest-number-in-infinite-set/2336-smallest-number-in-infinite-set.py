class SmallestInfiniteSet:

    def __init__(self):
        self.present = [True for _ in range(1001)]

    def popSmallest(self) -> int:
        for i in range(1001):
            if self.present[i]:
                self.present[i] = False
                return i + 1

    def addBack(self, num: int) -> None:
        self.present[num - 1] = True


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)