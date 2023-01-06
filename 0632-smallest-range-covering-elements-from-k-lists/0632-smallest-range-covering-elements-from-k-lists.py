class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr = [(nums[i][j], i) for i in range(len(nums)) for j in range(len(nums[i]))]
        arr.sort()
        
        smallest_range = [arr[0][0], arr[-1][0]]
        distinct_count = [0 for i in range(len(nums))]
        left = 0
        right = 0
        while right < len(arr):
            distinct_count[arr[right][1]] += 1
            while all(distinct_count):
                if arr[right][0] - arr[left][0] < smallest_range[1] - smallest_range[0]:
                    smallest_range = [arr[left][0], arr[right][0]]
                distinct_count[arr[left][1]] -= 1
                left += 1
            right += 1
        
        return smallest_range