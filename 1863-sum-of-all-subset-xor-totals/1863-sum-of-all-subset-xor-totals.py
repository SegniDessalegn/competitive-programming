class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def xor_total(nums):
            xor = 0
            for num in nums:
                xor ^= num
            return xor
        
        def find_ans(nums, curr):
            ans = xor_total(curr)
            for i in range(len(nums)):
                curr.append(nums[i])
                ans += find_ans(nums[i + 1:], curr)
                curr.pop()
            
            return ans
        
        return find_ans(nums, [])
    