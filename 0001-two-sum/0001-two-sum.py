class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, val in enumerate(nums):
            x = target - val
            if x not in index_map:
                index_map[target - x] = i
            else:
                return [i, index_map[x]]