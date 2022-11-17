class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        counts = Counter(nums)
        i, j = 0, counts[1]
        curr = Counter(nums[:j])[0]
        res = curr
        while i < len(nums):
            j_idx = j
            if j >= len(nums):
                j_idx = j - len(nums)
            if nums[j_idx] == 0:
                curr += 1
            if nums[i] == 0:
                curr -= 1
            res = min(res, curr)
            i += 1
            j += 1
        return res