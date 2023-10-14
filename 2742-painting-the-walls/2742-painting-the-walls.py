class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @cache
        def get_ans(i, available_time):
            if available_time >= N:
                return 0
            
            if i == N:
                return float("inf")
            
            curr_cost = float("inf")
            # choose this wall for paid painter
            curr_cost = min(curr_cost, cost[i] + get_ans(i + 1, 1 + available_time + time[i]))
            
            # choose this wall for the free painter
            curr_cost = min(curr_cost, get_ans(i + 1, available_time))
            
            return curr_cost
        
        
        N = len(cost)
        return get_ans(0, 0)