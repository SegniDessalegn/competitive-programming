class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = nums[k]
        _min = nums[k]
        left = k - 1
        right = k + 1
        while left >= 0 or right < N:
            if left >= 0 and right < N:
                if nums[left] < nums[right]:
                    _min = min(_min, nums[right])
                    right += 1
                else:
                    _min = min(_min, nums[left])
                    left -= 1
            elif left >= 0:
                _min = min(_min, nums[left])
                left -= 1
            else:
                _min = min(_min, nums[right])
                right += 1
            ans = max(ans, _min * (right - left - 1))
        
        return ans
    