class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        mod = 1000000007
        count = [0] * 101
        for i in arr:
            count[i] += 1
        for i in range(101):
            for j in range(101):
                k = target - i - j
                if k < 0 or k > 100:
                    continue
                if i == j == k:
                    ans += count[i] * (count[i] - 1) * (count[i] - 2) / 6
                elif i == j != k:
                    ans += count[i] * (count[i] - 1) * count[k] / 2
                elif i < j < k:
                    ans += count[i] * count[j] * count[k]
        return int(ans % mod)