class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # union find
        
        reps = {i:i for i in range(len(s))}
        def find(x):
            nodes = []
            while x != reps[x]:
                nodes.append(x)
                x = reps[x]
            for n in nodes:
                reps[n] = x
            return x
        
        def union(x, y):
            if y < x:
                x, y = y, x
            x_rep = find(x)
            while y != reps[y]:
                temp = reps[y]
                reps[y] = x_rep
                y = temp
            reps[y] = x_rep
        
        for p in pairs:
            union(p[0], p[1])
            
        for rep in reps:
            reps[rep] = find(rep)
        
        group = defaultdict(list)
        for rep in reps:
            group[reps[rep]].append(rep)
        
        for g in group:
            group[g].sort(key = lambda i: s[i])
        
        ans = ["" for _ in range(len(s))]
        for g in group:
            sorted_index = sorted(group[g])
            for i in range(len(sorted_index)):
                ans[sorted_index[i]] = s[group[g][i]]
        
        return "".join(ans)