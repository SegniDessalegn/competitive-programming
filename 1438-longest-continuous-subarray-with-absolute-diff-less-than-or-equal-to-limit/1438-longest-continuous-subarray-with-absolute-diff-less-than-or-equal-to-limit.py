class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = Deque()
        max_queue = Deque()
        longest = 0
        i = 0
        for index,n in enumerate(nums):
            while min_queue and min_queue[-1] > n:
                min_queue.pop()
            min_queue.append(n)
            while max_queue and max_queue[-1] < n:
                max_queue.pop()
            max_queue.append(n)
            while max_queue[0] - min_queue[0] > limit:
                if min_queue[0] == nums[i]:
                    min_queue.popleft()
                if max_queue[0] == nums[i]:
                    max_queue.popleft()
                i += 1
            longest = max(longest, index - i + 1)
        return longest