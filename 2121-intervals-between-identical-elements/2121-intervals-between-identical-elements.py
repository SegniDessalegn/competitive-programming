class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        indices = {}
        pref_sums = {}
        for i in range(len(arr)):
            if arr[i] not in indices:
                indices[arr[i]] = []
                pref_sums[arr[i]] = [0]
            indices[arr[i]].append(i)
            pref_sums[arr[i]].append(pref_sums[arr[i]][-1] + i)
        ans = [0] * len(arr)
        for n in indices:
            l = len(pref_sums[n])
            for i in range(len(indices[n])):
                right_sum = pref_sums[n][-1] - pref_sums[n][i + 1] - (indices[n][i] * (l - i - 2))
                left_sum = pref_sums[n][i] - (i * indices[n][i])
                ans[indices[n][i]] = right_sum - left_sum
        return ans