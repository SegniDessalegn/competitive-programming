class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}
        i, j = 0, 0
        while j < len(nums):
            count[nums[j]] = count.get(nums[j], 0) + 1
            if count[nums[j]] > 1:
                return True
            if j - i >= k:
                count[nums[i]] -= 1
                i += 1
            j += 1
        return False