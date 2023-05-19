class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # union find
        
        n = len(stones)
        for i in range(n):
            stones[i] = tuple(stones[i])
        
        reps = {stone:stone for stone in stones}
        
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
            while y != reps[y]:
                temp = reps[y]
                reps[y] = x_rep
                y = temp
            reps[y] = x_rep
            
        stones.sort()
        for i in range(1, n):
            if stones[i][0] == stones[i - 1][0]:
                union(stones[i], stones[i - 1])
        
        stones.sort(key = lambda stone: stone[1])
        for i in range(1, n):
            if stones[i][1] == stones[i - 1][1]:
                union(stones[i], stones[i - 1])
        
        for r in reps:
            find(r)
        
        components = defaultdict(int)
        for rep in reps:
            components[reps[rep]] += 1
        
        count = 0
        for comp in components.values():
            count += comp - 1
        
        return count