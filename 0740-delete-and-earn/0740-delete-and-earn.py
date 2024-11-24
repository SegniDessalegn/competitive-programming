class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        N = len(nums)
        
        def get_index(index):
            for i in range(index + 1, N):
                if nums[i] != nums[index] + 1:
                    return i
            return N
        
        @cache
        def get_ans(i):
            if i == N:
                return 0
            
            # pick
            pick = (nums[i] * count[nums[i]]) + get_ans(get_index(i))
            
            # not pick
            not_pick = get_ans(i + 1)
            
            return max(pick, not_pick)
        
        
        return get_ans(0)
        