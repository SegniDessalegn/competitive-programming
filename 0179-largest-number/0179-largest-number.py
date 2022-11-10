class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = self.custom_merge_sort(nums)
        return ''.join(l) if l[0] != "0" else "0"

    def custom_merge_sort(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return [str(nums[0])]
        half = len(nums) // 2
        first_half = self.custom_merge_sort(nums[:half])
        second_half = self.custom_merge_sort(nums[half:])
        i, j = 0, 0
        sorted_list = []
        while i < len(first_half) and j < len(second_half):
            if first_half[i] + second_half[j] >= second_half[j] + first_half[i]:
                sorted_list.append(first_half[i])
                i += 1
            else:
                sorted_list.append(second_half[j])
                j += 1
        if i <= len(first_half):
            sorted_list += first_half[i:]
        if j <= len(second_half):
            sorted_list += second_half[j:]
        return sorted_list