class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        right_sum = sum(satisfaction)
        coefficient = 0
        for i in range(len(satisfaction)):
            coefficient += ((i + 1) * satisfaction[i])
        
        max_coefficient = coefficient
        for i in range(len(satisfaction)):
            right_sum -= satisfaction[i]
            coefficient -= (satisfaction[i] + right_sum)
            max_coefficient = max(max_coefficient, coefficient)
        
        return max(0, max_coefficient)