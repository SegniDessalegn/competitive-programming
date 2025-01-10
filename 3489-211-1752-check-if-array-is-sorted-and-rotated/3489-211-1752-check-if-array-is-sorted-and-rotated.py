class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        invalid = False
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                if invalid:
                    return False
                invalid = True
        
        return not invalid or nums[0] >= nums[N - 1]
    