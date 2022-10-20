class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        count = 0
        covered = {}
        for i in ranges:
            for j in range(max(left, i[0]), min(right, i[1]) + 1):
                covered[j] = covered.get(j, 0) + 1
                if covered[j] == 1:
                    count += 1
        return True if count == right - left + 1 else False