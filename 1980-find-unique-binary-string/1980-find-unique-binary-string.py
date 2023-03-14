class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def recur(b = []):
            nonlocal nums
            if len(b) == len(nums):
                b = "".join(b)
                if b not in nums:
                    return b
                return
            
            for i in range(2):
                b.append(str(i))
                res = recur(b)
                if res:
                    return res
                b.pop()
            
        nums = set(nums)
        return recur()