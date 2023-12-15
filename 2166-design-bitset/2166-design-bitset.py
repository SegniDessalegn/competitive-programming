class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.dict = defaultdict(int)
        self.idx_flipped_count = defaultdict(int)
        self.flipped_count = 0
        self.setbits = 0

    def fix(self, idx: int) -> None:
        
        if self.idx_flipped_count[idx] % 2 != self.flipped_count % 2:
            self.dict[idx] = 1 - self.dict[idx]
        
        if self.dict[idx] == 0:
            self.setbits += 1
        
        self.dict[idx] = 1
        self.idx_flipped_count[idx] = self.flipped_count

    def unfix(self, idx: int) -> None:
        if self.idx_flipped_count[idx] % 2 != self.flipped_count % 2:
            self.dict[idx] = 1 - self.dict[idx]
        
        if self.dict[idx] == 1:
            self.setbits -= 1
        
        self.dict[idx] = 0
        self.idx_flipped_count[idx] = self.flipped_count

    def flip(self) -> None:
        self.setbits = self.size - self.setbits
        self.flipped_count += 1

    def all(self) -> bool:
        return self.setbits == self.size

    def one(self) -> bool:
        return self.setbits > 0

    def count(self) -> int:
        return self.setbits

    def toString(self) -> str:
        arr = []
        for idx in range(self.size):
            if self.idx_flipped_count[idx] % 2 != self.flipped_count % 2:
                self.dict[idx] = 1 - self.dict[idx]
                self.idx_flipped_count[idx] = self.flipped_count
            arr.append(str(self.dict[idx]))
        
        return "".join(arr)
    

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()