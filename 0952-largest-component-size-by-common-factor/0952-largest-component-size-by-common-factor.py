class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        reps = {}
        rank = {}
        def find(x):
            nodes = []
            while x != reps[x]:
                nodes.append(x)
                x = reps[x]
            
            for node in nodes:
                reps[node] = x
            
            return x
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
            if x_rep != y_rep:
                rank[y_rep] += rank[x_rep]
            reps[x_rep] = y_rep
        
        def get_prime_factors(num):
            factorization = set()
            d = 2
            while d * d <= num:
                while num % d == 0:
                    factorization.add(d)
                    num //= d
                d += 1
            if num > 1:
                factorization.add(num)
            
            return factorization
        
        for num in nums:
            if num == 1:
                continue
            prime_factors = list(get_prime_factors(num))
            for p in prime_factors:
                if p not in reps:
                    reps[p] = p
                    rank[p] = 0
            
            for i in range(1, len(prime_factors)):
                union(prime_factors[i], prime_factors[i - 1])
            
            rank[find(prime_factors[0])] += 1
        
        return max(rank.values())
        