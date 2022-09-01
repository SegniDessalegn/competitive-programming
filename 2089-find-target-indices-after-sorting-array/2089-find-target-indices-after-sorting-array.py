class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        starting_index = 0
        equal_counter = 0
        for i in range(len(nums)):
            if nums[i] < target:
                starting_index += 1
            if nums[i] == target:
                equal_counter += 1
        return [i + starting_index for i in range(equal_counter)]