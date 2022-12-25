class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for d in digits:
            num += str(d)
        num = int(num) + 1
        incremented = []
        for d in str(num):
            incremented.append(int(d))
        return incremented