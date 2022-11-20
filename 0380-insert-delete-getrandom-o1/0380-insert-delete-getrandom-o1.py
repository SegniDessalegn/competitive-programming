import random

class RandomizedSet:

    def __init__(self):
        self.items = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.items:
            index = self.items[val]
            self.items[self.arr[-1]] = index
            self.items.pop(val)
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()