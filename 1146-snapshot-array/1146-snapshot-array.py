class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[(0, 0)] for _ in range(length)]
        self.snap_count = 0

    def set(self, index: int, val: int) -> None:
        if self.array[index][-1][0] == self.snap_count:
            self.array[index][-1] = (self.snap_count, val)
        else:
            self.array[index].append((self.snap_count, val))

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.array[index]
        i = bisect.bisect(snaps, (snap_id + 1,)) - 1
        return snaps[i][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)