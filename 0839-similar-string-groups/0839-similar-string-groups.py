class UnionFind:
    
    def __init__(self, items):
        self.reps = {item:item for item in items}
    
    def find(self, x):
        if x != self.reps[x]:
            self.reps[x] = self.find(self.reps[x])
        return self.reps[x]
    
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        self.reps[x_rep] = y_rep


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        U = UnionFind(strs)
        
        for word1 in strs:
            for word2 in strs:
                if self.is_valid(word1, word2):
                    U.union(word1, word2)
        
        groups = set()
        for word in strs:
            groups.add(U.find(word))
        
        return len(groups)
    
    
    def is_valid(self, word1, word2):
        count = 0
        w1 = []
        w2 = []
        for i in range(len(word1)):
            if word2[i] != word1[i]:
                count += 1
                w1.append(word1[i])
                w2.append(word2[i])

        return count == 0 or (count == 2 and w1[0] == w2[1] and w1[1] == w2[0])
