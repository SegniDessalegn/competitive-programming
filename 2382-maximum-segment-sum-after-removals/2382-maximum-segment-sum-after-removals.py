class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        n = len(nums)
        reps = [i for i in range(n)]
        rank = [0 for i in range(n)]
        
        def find(x):
            if reps[x] != x:
                reps[x] = find(reps[x])
            return reps[x]
        
        def union(x, y):
            nonlocal max_rank
            x_rep = find(x)
            y_rep = find(y)
            
            reps[x_rep] = y_rep
            rank[y_rep] += rank[x_rep]
            max_rank = max(max_rank, rank[y_rep])
        
        ans = [0]
        curr = [0] * n
        max_rank = 0
        for i in range(n - 1, -1, -1):
            idx = removeQueries[i]
            
            rank[idx] = nums[idx]
            max_rank = max(max_rank, rank[idx])
            
            if idx - 1 >= 0 and curr[idx - 1] != 0:
                union(idx, idx - 1)
            if idx + 1 < n and curr[idx + 1] != 0:
                union(idx, idx + 1)
            
            ans.append(max_rank)
            curr[idx] = nums[idx]
            
        
        return ans[-2::-1]