class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        pre_sum = 0
        for i in gain:
            pre_sum += i
            highest = max(highest, pre_sum)
        return highest