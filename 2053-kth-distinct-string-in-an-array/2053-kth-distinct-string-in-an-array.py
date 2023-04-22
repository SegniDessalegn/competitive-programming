class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        ans = ""
        for s in arr:
            if count[s] == 1:
                k -= 1
                if k == 0:
                    ans = s
                    break
        return ans