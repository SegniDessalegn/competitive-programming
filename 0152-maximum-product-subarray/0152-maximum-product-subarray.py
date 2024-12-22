class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def get_prodcut_without_zeros(i, j):
            if i > j:
                return 0
            
            prefix = [nums[i]]
            for k in range(i + 1, j + 1):
                prefix.append(prefix[-1] * nums[k])
            prefix = [-float("inf")] + prefix
            
            suffix = [nums[j]]
            for k in range(j - 1, i - 1, -1):
                suffix.append(suffix[-1] * nums[k])
            suffix.append(-float("inf"))
            suffix = suffix[::-1]
            
            result = -float("inf")
            for k in range(len(prefix) - 1):
                result = max(result, prefix[k + 1], prefix[k], suffix[k + 1], suffix[k])
            
            return result
                
        prev = -1
        result = get_prodcut_without_zeros(0, len(nums) - 1)
        for i in range(len(nums)):
            if nums[i] == 0:
                result = max(result, nums[i], get_prodcut_without_zeros(prev + 1, i - 1))
                prev = i
        
        result = max(result, get_prodcut_without_zeros(prev + 1, len(nums) - 1))
        
        return result
    