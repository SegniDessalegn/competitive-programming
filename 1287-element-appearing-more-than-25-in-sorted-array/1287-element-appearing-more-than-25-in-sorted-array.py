class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        return sorted(arr, key = lambda num: count[num])[-1]
    