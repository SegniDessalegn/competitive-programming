class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        N = len(nums1)
        freq = Counter(nums4)
        
        @cache
        def two_sum(target):
            curr_count = 0
            for n in nums3:
                if target - n in freq:
                    curr_count += freq[target - n]
            
            return curr_count
        
        count = 0
        for i in range(N):
            for j in range(N):
                count += two_sum(-nums1[i] - nums2[j])
        
        return count