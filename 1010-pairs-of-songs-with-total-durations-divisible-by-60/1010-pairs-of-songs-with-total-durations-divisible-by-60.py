class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem = defaultdict(int)
        for t in time:
            rem[t % 60] += 1
        
        count = 0
        for i in range(1, 30):
            count += rem[i] * rem[60 - i]
        
        count += ((rem[0] * (rem[0] - 1)) // 2)
        count += ((rem[30] * (rem[30] - 1)) // 2)
        
        return count