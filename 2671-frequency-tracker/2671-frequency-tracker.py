class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq_freq[self.freq[number]] -= 1
        self.freq_freq[self.freq[number]] = max(0, self.freq_freq[self.freq[number]])
        self.freq[number] += 1
        self.freq_freq[self.freq[number]] += 1
        

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            self.freq_freq[self.freq[number]] -= 1
            self.freq_freq[self.freq[number]] = max(0, self.freq_freq[self.freq[number]])
            self.freq[number] -= 1
            self.freq_freq[self.freq[number]] += 1
            if self.freq[number] == 0:
                self.freq.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)