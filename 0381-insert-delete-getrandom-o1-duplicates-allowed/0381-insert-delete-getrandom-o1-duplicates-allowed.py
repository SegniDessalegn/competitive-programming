import random

class RandomizedCollection:

    def __init__(self):
        self.items = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.items:
            self.items[val].add(len(self.arr))
            self.arr.append(val)
            return False
        self.items[val] = set([len(self.arr)])
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.items:
            for index in self.items[val]:
                break
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            self.items[val].remove(index)
            if len(self.items[val]) == 0:
                self.items.pop(val)
            if index != len(self.arr) - 1:
                self.items[self.arr[index]].remove(len(self.arr) - 1)
                self.items[self.arr[index]].add(index)
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()