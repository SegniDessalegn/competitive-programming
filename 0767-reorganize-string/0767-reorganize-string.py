class Solution:
    def reorganizeString(self, s: str) -> str:
        # heap
        # choose the most frequent characters every time
        
        count = Counter(s)
        
        heap = []
        for char in count:
            heappush(heap, (-count[char], char))
        
        ans = []
        while heap:
            curr = heapq.heappop(heap)
            if ans and curr[1] == ans[-1]:
                if not heap:
                    return ""
                curr2 = heapq.heappop(heap)
                ans.append(curr2[1])
                if -curr2[0] > 1:
                    heapq.heappush(heap, (curr2[0] + 1, curr2[1]))
            
            ans.append(curr[1])
            if -curr[0] > 1:
                heapq.heappush(heap, (curr[0] + 1, curr[1]))
            
        return "".join(ans)