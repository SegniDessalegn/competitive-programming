class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        prev = defaultdict(int)
        nums.sort()
        
        for n in nums:
            prev[n % space] += 1
        
        num, max_count = -1, 0
        for n in prev:
            if prev[n] > max_count:
                num = n
                max_count = prev[n]
        
        for n in nums:
            if abs(n - num) % space == 0:
                return n
