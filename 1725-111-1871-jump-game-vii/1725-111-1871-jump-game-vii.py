class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        queue = [0]
        max_reachable = 0
        for i in queue:
            start = max(max_reachable + 1, i + minJump)
            for j in range(start, min(i + maxJump + 1, N)):
                if s[j] == "0":
                    queue.append(j)
                    if j == N - 1:
                        return True
            max_reachable = i + maxJump
        
        return False
    