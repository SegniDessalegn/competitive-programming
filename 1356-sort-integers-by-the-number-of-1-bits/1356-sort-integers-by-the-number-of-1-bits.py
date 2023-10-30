class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num: (bin(num)[2:].count("1"), num))