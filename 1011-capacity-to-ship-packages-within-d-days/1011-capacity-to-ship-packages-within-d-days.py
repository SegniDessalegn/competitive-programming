class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights) - 1
        high = sum(weights) + 1
        while high - low > 1:
            mid = (low + high) // 2
            if self.check_weight(weights, mid) < days:
                high = mid
            else:
                low = mid
        
        return high
    
    
    def check_weight(self, weights, weight):
        days = 0
        curr_sum = 0
        for n in weights:
            curr_sum += n
            if curr_sum > weight:
                curr_sum = n
                days += 1
        
        return days