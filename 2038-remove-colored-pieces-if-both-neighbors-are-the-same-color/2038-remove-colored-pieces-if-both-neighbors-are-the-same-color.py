class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        colors += "C"
        prev = None
        count = 0
        for i in range(len(colors)):
            if prev == colors[i]:
                count += 1
            else:
                if prev == "A":
                    alice += max(0, count - 2)
                else:
                    bob += max(0, count - 2)
                count = 1
                prev = colors[i]
        
        return alice > bob