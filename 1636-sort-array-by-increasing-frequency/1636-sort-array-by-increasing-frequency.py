class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        nums.sort()
        freq = defaultdict(list)
        for n in nums:
            freq[count[n]].append(n)
        
        for f in freq:
            freq[f].sort(reverse = True)
        
        arr = []
        for f in freq:
            arr.append(f)
        arr.sort()
        
        ans = []
        for f in arr:
            for n in freq[f]:
                ans.append(n)
        
        return ans