class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for n in count:
            if count[n] == 1 and n + 1 not in count and n - 1 not in count:
                ans.append(n)
        return ans