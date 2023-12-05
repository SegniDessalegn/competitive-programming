class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return ([""] + sorted([num[i - 2] + num[i - 1] + num[i] for i in range(2, len(num)) if num[i - 2] == num[i - 1] == num[i]]))[-1]