class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.findNthS(n)[k - 1]
        
    def findNthS(self, n):
        if n == 1:
            return "0"
        s = self.findNthS(n - 1)
        return s + "1" + self.invert(s)[::-1]
        
    def invert(self, bits):
        inverted = ""
        for i in bits:
            if i == "1":
                inverted += "0"
            else:
                inverted += "1"
        return inverted