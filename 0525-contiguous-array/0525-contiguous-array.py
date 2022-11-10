class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = 0
        index_map = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                s -= 1
            else:
                s += 1
            if s == 0:
                ans = i + 1
            if s in index_map:
                ans = max(ans, i - index_map[s])
            else:
                index_map[s] = i
        return ans