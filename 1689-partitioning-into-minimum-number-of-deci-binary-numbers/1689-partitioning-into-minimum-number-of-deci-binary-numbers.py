class Solution:
    def minPartitions(self, n: str) -> int:
        deci_binaries = 0
        for d in n:
            if int(d) > deci_binaries:
                deci_binaries = int(d)
        return deci_binaries