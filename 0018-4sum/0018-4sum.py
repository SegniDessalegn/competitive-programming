class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        def two_sum(start, target):
            ans = []
            left = start
            right = N - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    ans.append([left, right])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1 
                    left += 1
                    right -= 1
                elif curr_sum > target:
                    right -= 1
                else:
                    left += 1
            
            return ans
        
        ans = set()
        nums.sort()
        for a in range(N):
            for b in range(a + 1, N):
                curr_ans = two_sum(b + 1, target - nums[a] - nums[b])
                for c, d in curr_ans:
                    ans.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
        
        return list(ans)