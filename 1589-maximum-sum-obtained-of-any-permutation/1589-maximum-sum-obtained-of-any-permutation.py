class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        max_index = requests[0][1]
        for r in requests:
            max_index = max(max_index, r[1])
        
        ranges = [0] * (max_index + 2)
        
        for r in requests:
            ranges[r[0]] += 1
            ranges[r[1] + 1] -= 1
        
        for i in range(1, len(ranges)):
            ranges[i] += ranges[i - 1]
        
        nums.sort(reverse = True)
        ranges.sort(reverse = True)
        
        i = 0
        max_sum = 0
        while ranges[i] != 0:
            max_sum += (nums[i] * ranges[i])
            i += 1
        
        return max_sum % (10**9 + 7)