class RabinKarpHash:
    def __init__(self, base=27, prime=(2 ** 31) - 1):
        self.base = base
        self.prime = prime
        self.hash = 0
        self.length = 0

    def add_last(self, char):
        self.hash = (self.hash * self.base + (ord(char) - ord("a") + 1)) % self.prime
        self.length += 1

    def remove_front(self, char):
        if self.length == 0:
            return
        front_char_value = (ord(char) - ord("a") + 1) * pow(self.base, self.length - 1, self.prime)
        self.hash = (self.hash - front_char_value) % self.prime
        self.length -= 1


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        N = len(s)
        H = RabinKarpHash(base = power, prime = modulo)
        
        for i in range(N - 1, N - k - 1, -1):
            H.add_last(s[i])
        
        start_index = i
        for i in range(N - k - 1, -1, -1):
            H.add_last(s[i])
            H.remove_front(s[i + k])
            
            if H.hash == hashValue:
                start_index = i
            
        return s[start_index:start_index + k]