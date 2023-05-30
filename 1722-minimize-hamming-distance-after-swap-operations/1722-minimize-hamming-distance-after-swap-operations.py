class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # union find
        
        reps = {i:i for i in range(len(source))}
        def find(x):
            while x != reps[x]:
                x = reps[x]
            return x
        
        def union(x, y):
            x_rep = find(x)
            while y != reps[y]:
                temp = reps[y]
                reps[y] = x_rep
                y = temp
            reps[y] = x_rep
        
        n = len(source)
        indexes = defaultdict(list)
        for i in range(n):
            indexes[source[i]].append(i)
        
        for swaps in allowedSwaps:
            union(swaps[0], swaps[1])
        
        same = 0
        swapped = set()
        for i in range(n):
            i_rep = find(i)
            for index in indexes[target[i]]:
                if index not in swapped and i_rep == find(index):
                    same += 1
                    swapped.add(index)
                    break
        
        return n - same