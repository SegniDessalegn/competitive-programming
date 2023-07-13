class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ab = 0
        c = 0
        for i in range(len(a) - 1, -1, -1):
            if a[i] == "1":
                ab += 2 ** c
            c += 1
        
        bb = 0
        c = 0
        for i in range(len(b) - 1, -1, -1):
            if b[i] == "1":
                bb += 2 ** c
            c += 1
        
        return bin(ab + bb)[2:]