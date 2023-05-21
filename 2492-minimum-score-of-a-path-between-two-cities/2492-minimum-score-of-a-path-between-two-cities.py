class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # union find
        # make 1 parent always
        # if representative of any node is 1, then there is a path between 1 and the node and we can minimize the cost here
        # we are assured that there is always a path between 1 and n node
        
        reps = {i:i for i in range(1, n + 1)}
        def find(x):
            nodes = []
            while x != reps[x]:
                nodes.append(x)
                x = reps[x]
            for n in nodes:
                reps[n] = x
            return x
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            if y_rep == 1:
                x_rep, y_rep = y_rep, x_rep
            reps[y_rep] = x_rep
        
        
        for road in roads:
            a, b, c = road
            union(a, b)
        
        ans = float("inf")
        for road in roads:
            a, b, c = road
            if find(a) == 1 or find(b) == 1:
                ans = min(ans, c)
        
        return ans