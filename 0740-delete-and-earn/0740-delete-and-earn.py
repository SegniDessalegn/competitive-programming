class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        N = len(nums)
        
        prev = nums[0] * count[nums[0]]
        prev_prev = 0
        
        for i in range(1, N):
            if nums[i] == nums[i - 1] + 1:
                curr = max((nums[i] * count[nums[i]]) + prev_prev, prev)
            else:
                curr = (nums[i] * count[nums[i]]) + max(prev_prev, prev)
            
            prev, prev_prev = curr, prev
        
        return max(prev, prev_prev)
        