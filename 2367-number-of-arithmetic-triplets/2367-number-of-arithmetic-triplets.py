class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        cnt = 0
        for n in s:
            if n - diff in s and n - (diff * 2) in s:
                cnt += 1
        return cnt