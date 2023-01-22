class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        dist_sub = set()
        count = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] % p == 0:
                count += 1
            while count > k:
                if nums[left] % p == 0:
                    count -= 1
                left += 1
            i = left
            while i <= right:
                dist_sub.add(tuple(nums[i:right + 1]))
                i += 1
            right += 1
        
        return len(dist_sub)