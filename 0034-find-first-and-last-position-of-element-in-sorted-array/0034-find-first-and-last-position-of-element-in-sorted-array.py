class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        pos = []
        left, right = 0, len(nums) - 1
        if nums[left] == target:
            pos.append(left)
        else:
            while left <= right:
                index = (left + right) // 2
                if nums[index] < target:
                    left = index + 1
                else:
                    right = index - 1
            if left >= len(nums) or right < 0 or nums[left] != target:
                return [-1, -1]
            pos.append(left)
        
        left, right = 0, len(nums) - 1
        if nums[right] == target:
            pos.append(right)
        else:
            while left <= right:
                index = (left + right) // 2
                if nums[index] <= target:
                    left = index + 1
                else:
                    right = index - 1
            pos.append(right)
        return pos
        