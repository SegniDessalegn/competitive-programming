class UnionFind:
    def __init__(self, n):
        self.reps = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}
    
    def find(self, x):
        if x != self.reps[x]:
            self.reps[x] = self.find(self.reps[x])
        return self.reps[x]
    
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        
        self.reps[x_rep] = y_rep
        self.rank[y_rep] += self.rank[x_rep]
        if x_rep != y_rep:
            self.rank[y_rep] += 1

class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.U = UnionFind(n)
        self.uploaded = [False for _ in range(n)]

    def upload(self, video: int) -> None:
        video -= 1 # convert it to zero indexed
        
        self.uploaded[video] = True
        if video > 0 and self.uploaded[video - 1]:
            self.U.union(video, video - 1)
        
        if video < self.n - 1 and self.uploaded[video + 1]:
            self.U.union(video, video + 1)

    def longest(self) -> int:
        if self.uploaded[0]:
            return self.U.rank[self.U.find(0)] + 1
        return 0


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()