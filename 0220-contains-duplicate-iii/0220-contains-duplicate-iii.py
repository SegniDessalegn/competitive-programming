from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        curr_list = SortedList()
        left, right = 0, 0
        while right < len(nums):
            if right > indexDiff:
                curr_list.remove(nums[left])
                left += 1
            pos1 = bisect_left(curr_list, nums[right] - valueDiff)
            pos2 = bisect_right(curr_list, nums[right] + valueDiff)
            if pos1 != pos2:
                return True
            curr_list.add(nums[right])
            right += 1
        return False