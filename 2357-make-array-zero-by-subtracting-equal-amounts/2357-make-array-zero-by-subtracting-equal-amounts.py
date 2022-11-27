class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        duplicates = set()
        counter = 0
        for n in nums:
            if n != 0 and n not in duplicates:
                counter += 1
            duplicates.add(n)
        return counter