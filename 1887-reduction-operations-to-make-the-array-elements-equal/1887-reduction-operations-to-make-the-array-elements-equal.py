class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        N = len(nums)
        ops = 0
        for i in range(N - 1, 0, -1):
            ops += count[nums[i]]
            count[nums[i - 1]] += count[nums[i]]
        
        return ops
    