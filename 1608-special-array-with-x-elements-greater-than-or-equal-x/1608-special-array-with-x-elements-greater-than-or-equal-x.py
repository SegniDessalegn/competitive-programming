class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(nums[-1] + 1):
            left, right = 0, n - 1
            while left <= right:
                index = (left + right) // 2
                if nums[index] < i:
                    left = index + 1
                else:
                    right = index - 1
            if n - left == i:
                return i
        return -1