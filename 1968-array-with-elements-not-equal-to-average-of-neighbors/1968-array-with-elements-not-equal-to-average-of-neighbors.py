class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        new_list = []
        for i in range(len(nums)//2):
            new_list.append(nums[i])
            new_list.append(nums[-1 - i])
        if len(nums) % 2 != 0:
            new_list.append(nums[-2 - i])
        return new_list