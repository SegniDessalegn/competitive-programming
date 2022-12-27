class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = set()
        def rec(i):
            if i >= len(nums) - 1:
                return True
            if i in memo:
                return False
            for idx in range(i + 1, i + nums[i] + 1):
                if idx in memo:
                    continue
                if i >= len(nums) - 1 or rec(idx):
                    return True
                memo.add(idx)
            memo.add(i)
            return False
        return rec(0)