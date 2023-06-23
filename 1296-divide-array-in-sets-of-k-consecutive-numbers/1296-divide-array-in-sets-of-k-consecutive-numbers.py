class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        
        nums.sort()
        ending = defaultdict(list)
        for n in nums:
            length = 1
            if ending[n - 1]:
                length += heapq.heappop(ending[n - 1])
            if length < k:
                heapq.heappush(ending[n], length)
        
        for arr in ending:
            for n in ending[arr]:
                if n % k != 0:
                    return False
        
        return True