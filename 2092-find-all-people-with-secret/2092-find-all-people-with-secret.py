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
    def findAllPeople(self, N: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        M = len(meetings)
        meetings.sort(key = lambda meeting: meeting[2])
        
        U = UnionFind([i for i in range(N)])
        U.union(0, firstPerson)
        
        j = 0
        prev_t = meetings[0][2]
        for i in range(M):
            p1, p2, t = meetings[i]
            if t != prev_t:
                k = j
                while j < i:
                    p1j, p2j, tj = meetings[j]
                    if U.find(0) == U.find(p1j) or U.find(0) == U.find(p2j):
                        U.union(p1j, p2j)
                    j += 1
                
                l = i - 1
                while l >= k:
                    p1l, p2l, tl = meetings[l]
                    if U.find(0) == U.find(p1l) or U.find(0) == U.find(p2l):
                        U.union(p1l, p2l)
                    l -= 1
                
                l = i - 1
                while l >= k:
                    p1l, p2l, tl = meetings[l]
                    if U.find(0) == U.find(p1l) or U.find(0) == U.find(p2l):
                        U.union(p1l, p2l)
                    l -= 1
                
                prev_t = t
            
            if U.find(0) == U.find(p1) or U.find(0) == U.find(p2):
                U.union(p1, p2)
        
        k = j
        while j <= i:
            p1j, p2j, tj = meetings[j]
            if U.find(0) == U.find(p1j) or U.find(0) == U.find(p2j):
                U.union(p1j, p2j)
            j += 1
        
        l = i
        while l >= k:
            p1l, p2l, tl = meetings[l]
            if U.find(0) == U.find(p1l) or U.find(0) == U.find(p2l):
                U.union(p1l, p2l)
            l -= 1
        
        l = i
        while l >= k:
            p1l, p2l, tl = meetings[l]
            if U.find(0) == U.find(p1l) or U.find(0) == U.find(p2l):
                U.union(p1l, p2l)
            l -= 1
        
        ans = []
        for person in range(N):
            if U.find(person) == U.find(0):
                ans.append(person)
        
        return ans
    