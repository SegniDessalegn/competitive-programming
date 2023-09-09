class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        new_arr = [(n1, n2) for (n1, n2) in zip(nums1, nums2)]
        
        new_arr.sort(key = lambda X: -X[1])
        
        N = len(nums1)
        ans = 0
        heap = []
        curr_sum = 0
        for i in range(N):
            if len(heap) == k - 1:
                ans = max(ans, new_arr[i][1] * (new_arr[i][0] + curr_sum))
            heapq.heappush(heap, new_arr[i][0])
            
            curr_sum += new_arr[i][0]
            if len(heap) == k:
                curr_sum -= heapq.heappop(heap)
        
        return ans