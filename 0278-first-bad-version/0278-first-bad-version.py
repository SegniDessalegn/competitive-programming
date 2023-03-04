# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n
        while lower_bound <= upper_bound:
            curr = (lower_bound + upper_bound) // 2
            if isBadVersion(curr):
                upper_bound = curr - 1
            else:
                lower_bound = curr + 1
        return lower_bound
