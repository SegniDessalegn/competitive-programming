class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_queue = deque()
        for i in range(len(nums[:k])):
            while mono_queue and mono_queue[-1][0] < nums[i]:
                mono_queue.pop()
            mono_queue.append((nums[i], i))
        res = []
        left, right = 0, k
        while right < len(nums):
            res.append(mono_queue[0][0])
            if mono_queue[0][1] == left:
                mono_queue.popleft()
            while mono_queue and nums[right] > mono_queue[-1][0]:
                mono_queue.pop()
            mono_queue.append((nums[right], right))
            left += 1
            right += 1
        res.append(mono_queue.popleft()[0])
        return res
        