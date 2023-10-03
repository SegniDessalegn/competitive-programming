class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        @cache
        def get_ans(i, A, B):
            if i == N:
                if A == B:
                    return 0
                return float("inf")
            
            curr_min = float("inf")
            # add it to city A
            curr_min = min(curr_min, costs[i][0] + get_ans(i + 1, A + 1, B))
            
            # add it to city B
            curr_min = min(curr_min, costs[i][1] + get_ans(i + 1, A, B + 1))
            
            return curr_min
        
        N = len(costs)
        return get_ans(0, 0, 0)
