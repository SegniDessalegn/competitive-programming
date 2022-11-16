class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        start = int((num - 3) / 3)
        return [n for n in range(start, start + 3)] if ((start * 3) + 3) == num else []