class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        N = len(colors)
        alice = 0
        bob = 0
        for i in range(2, N):
            if colors[i - 2:i + 1] == "AAA":
                alice += 1
            if colors[i - 2:i + 1] == "BBB":
                bob += 1
        
        return alice > bob