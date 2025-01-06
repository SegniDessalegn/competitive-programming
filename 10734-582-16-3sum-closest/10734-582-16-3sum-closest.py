class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        ans = nums[0]
        diff = float("inf")
        for i in range(N):
            left, right = i + 1, N - 1
            while left < right:
                curr_sum = nums[left] + nums[right] + nums[i]
                if abs(target - curr_sum) < diff:
                    ans = curr_sum
                    diff = abs(target - curr_sum)
                
                if curr_sum <= target:
                    left += 1
                else:
                    right -= 1

        return ans
    