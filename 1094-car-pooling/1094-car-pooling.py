class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        recent = []
        curr = 0
        for i in range(len(trips)):
            while recent and recent[0][0] <= trips[i][1]:
                curr -= recent[0][1]
                heapq.heappop(recent)
            heapq.heappush(recent, (trips[i][2], trips[i][0]))
            curr += trips[i][0]
            if curr > capacity:
                return False
            i += 1
        return True