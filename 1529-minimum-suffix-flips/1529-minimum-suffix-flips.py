class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0 if target[0] == "0" else 1
        i = 1
        while i < len(target):
            while i < len(target) and target[i] == target[i - 1]:
                i += 1
            if i < len(target):
                flips += 1
            i += 1
        
        return flips