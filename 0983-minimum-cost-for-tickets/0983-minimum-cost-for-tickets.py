class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def get_cost(i):
            if i >= N:
                return 0
            
            curr_cost = float("inf")
            
            # choose 1-day pass
            curr_cost = min(curr_cost, costs[0] + get_cost(bisect_left(days, days[i] + 1)))
            
            # choose 7-day pass
            curr_cost = min(curr_cost, costs[1] + get_cost(bisect_left(days, days[i] + 7)))
            
            # choose 30-day pass
            curr_cost = min(curr_cost, costs[2] + get_cost(bisect_left(days, days[i] + 30)))
            
            return curr_cost
        
        N = len(days)
        return get_cost(0)
        