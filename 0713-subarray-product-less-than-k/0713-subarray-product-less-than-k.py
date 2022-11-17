class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        curr_product = 1
        counter = 0
        while j < len(nums):
            curr_product *= nums[j]
            while i <= j and curr_product >= k:
                curr_product /= nums[i]
                i += 1
            counter += j - i + 1
            j += 1
        return counter