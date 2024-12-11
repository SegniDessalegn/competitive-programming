class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[0, 0]] for _ in range(length)]
        self.can_update = set()
        self.snap_count = 0

    def set(self, index: int, val: int) -> None:
        if index in self.can_update:
            self.array[index][1] = val
            self.can_update.add(index)
        else:
            self.array[index].append([self.snap_count, val])

    def snap(self) -> int:
        self.can_update = set()
        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        left = 0
        right = len(self.array[index])
        
        while right - left > 1:
            mid = (right + left) // 2
            
            if self.array[index][mid][0] <= snap_id:
                left = mid
            else:
                right = mid
        
        return self.array[index][left][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)