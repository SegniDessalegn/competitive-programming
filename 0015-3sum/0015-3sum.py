class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for n in range(len(nums)):
            if ans and nums[n] == ans[-1][0]:
                continue
            if nums[n] > 0:
                return ans
            i, j = n + 1, len(nums) - 1
            while i < j:
                s = nums[i] + nums[j]
                if s < -nums[n]:
                    i += 1
                elif s > -nums[n]:
                    j -= 1
                else:
                    if not ans or not ((ans[-1][1] == nums[i] and ans[-1][2] == nums[j]) or (ans[-1][2] == nums[i] and ans[-1][1] == nums[j])):
                        ans.append([nums[n], nums[i], nums[j]])
                    i += 1
                    j -= 1
        return ans