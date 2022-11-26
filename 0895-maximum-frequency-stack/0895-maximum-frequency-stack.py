class FreqStack:

    def __init__(self):
        self.val_freq = {}
        self.freq_val = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.val_freq[val] = self.val_freq.get(val, 0) + 1
        if self.val_freq[val] not in self.freq_val:
            self.freq_val[self.val_freq[val]] = []
        self.freq_val[self.val_freq[val]].append(val)
        if self.val_freq[val] > self.max_freq:
            self.max_freq = self.val_freq[val]

    def pop(self) -> int:
        val = self.freq_val[self.max_freq].pop()
        self.val_freq[val] -= 1
        if len(self.freq_val[self.max_freq]) == 0:
            self.freq_val.pop(self.max_freq)
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()