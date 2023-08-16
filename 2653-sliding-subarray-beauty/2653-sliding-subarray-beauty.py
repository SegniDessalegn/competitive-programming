class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def get_smallest(count):
            curr_x = x
            for i in range(-50, 0):
                curr_x -= count[i]
                if curr_x <= 0:
                    return i
            return 0
        
        negs = defaultdict(int)
        for i in range(k):
            if nums[i] < 0:
                negs[nums[i]] += 1
        
        ans = [get_smallest(negs)]
        
        for i in range(k, len(nums)):
            if nums[i] < 0:
                negs[nums[i]] += 1
            if nums[i - k] < 0:
                negs[nums[i - k]] -= 1
            
            ans.append(get_smallest(negs))
        
        return ans