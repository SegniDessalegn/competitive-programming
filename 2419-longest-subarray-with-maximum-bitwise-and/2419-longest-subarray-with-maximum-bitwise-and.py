class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.append(0)
        largest = nums[0]
        prev = nums[0]
        ans = defaultdict(int)
        count = 1
        
        for i in range(1, len(nums)):
            largest = max(largest, nums[i])
            if prev == nums[i]:
                count += 1
            else:
                if prev >= largest:
                    ans[prev] = max(ans[prev], count)
                count = 1
            prev = nums[i]
        
        return ans[max(ans.keys())]