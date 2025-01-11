class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        mono_queue = deque()
        ans = []
        for i in range(N):
            if mono_queue and i - mono_queue[0][1] + 1 > k:
                mono_queue.popleft()
            while mono_queue and nums[i] > mono_queue[-1][0]:
                mono_queue.pop()
            
            mono_queue.append((nums[i], i))
            if i >= k - 1:
                ans.append(mono_queue[0][0])
        
        return ans
    