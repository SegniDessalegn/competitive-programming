class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort(reverse = True)
        s = sum(nums)
        ans = []
        for q in queries:
            i = 0
            curr_sum = 0
            while i < len(nums) and q < s - curr_sum:
                curr_sum += nums[i]
                i += 1
            ans.append(len(nums) - i)
        return ans