class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        pre_sum = [0]
        for c in chalk:
            pre_sum.append(pre_sum[-1] + c)
        s = k % pre_sum[-1]
        for i in range(len(pre_sum)):
            if pre_sum[i] > s:
                return i - 1