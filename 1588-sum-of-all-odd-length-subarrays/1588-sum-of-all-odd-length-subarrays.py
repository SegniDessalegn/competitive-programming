class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i, n in enumerate(arr):
            ans += (math.ceil(((len(arr) - i) * (i + 1))/2)) * n
        return ans