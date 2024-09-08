class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        M = len(nums1)
        N = len(nums2)
        
        heap = [(nums1[0] + nums2[0], 0, 0)]
        res = []
        visited = set()
        
        while len(res) < k and heap:
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            
            if i + 1 < M and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < N and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        
        return res