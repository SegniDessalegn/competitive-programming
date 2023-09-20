class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        if s < x:
            return -1
        
        # concatenate nums together
        nums = nums + nums
        N = len(nums)
        ans = []
        left = 0
        curr_sum = 0
        for right in range(N):
            curr_sum += nums[right]
            
            while curr_sum > x:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == x:
                # convert it to one indexed number
                ans.append((left + 1, right + 1))
        
        result = float("inf")
        half = N // 2
        for a, b in ans:
            # if half is in the range, then the subarray is a valid operation
            if a <= half <= b or a <= half + 1 <= b:
                result = min(result, b - a + 1)
        
        return result if result != float("inf") else -1