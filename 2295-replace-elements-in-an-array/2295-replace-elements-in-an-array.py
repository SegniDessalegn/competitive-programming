class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {nums[i]: i for i in range(len(nums))}
        for operation in operations:
            nums[index[operation[0]]] = operation[1]
            index[operation[1]] = index[operation[0]]
            index.pop(operation[0])
        return nums