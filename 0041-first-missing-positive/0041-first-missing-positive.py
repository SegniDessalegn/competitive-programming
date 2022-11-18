class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            counter = 0
            while counter < len(nums) and nums[i] != i + 1:
                if nums[i] - 1 >= len(nums) or nums[i] <= 0:
                    nums[i] = 0
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                counter += 1
            i += 1
        curr = 1
        for n in nums:
            if n == curr:
                curr += 1
            elif n != 0:
                return curr
        return curr
        