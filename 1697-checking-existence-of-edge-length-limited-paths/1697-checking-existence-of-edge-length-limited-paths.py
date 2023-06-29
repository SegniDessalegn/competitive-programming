class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reps = {i:i for i in range(n)}
        
        for i in range(len(queries)):
            queries[i] = queries[i] + [i]
        
        queries.sort(key=lambda X:X[2])
        edgeList.sort(key=lambda X:X[2])
        
        def find(x):
            nodes = []
            while x != reps[x]:
                x = reps[x]
                nodes.append(x)
            for n in nodes:
                reps[n] = x
            return x
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            reps[x_rep] = y_rep
        
        available = set()
        for edge in edgeList:
            available.add(edge[0])
            available.add(edge[1])
        
        ans = [False for _ in range(len(queries))]
        idx = 0
        for i in range(len(queries)):
            p, q, l, qi = queries[i]
            while idx < len(edgeList) and edgeList[idx][2] < l:
                union(edgeList[idx][0], edgeList[idx][1])
                idx += 1
            if find(p) == find(q):
                ans[qi] = True
            else:
                ans[qi] = False
        
        return ans