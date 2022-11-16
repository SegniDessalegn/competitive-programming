class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        start = set()
        for n in nums:
            if n - 1 not in nums:
                start.add(n)
        ans = 0
        for n in start:
            curr = n + 1
            curr_ans = 0
            while curr in nums:
                curr_ans += 1
                curr += 1
            ans = max(ans, curr_ans)
        if start:
            ans += 1
        return ans