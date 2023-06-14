class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        queue = deque()
        index = {hand[i]:[] for i in range(n)}
        for i in range(n):
            index[hand[i]].append(i)
            queue.append((hand[i], i))
        
        used = set()
        while queue:
            curr = queue[0][0]
            for i in range(groupSize):
                if curr not in index or len(index[curr]) == 0:
                    return False
                used.add(index[curr].pop())
                curr += 1
            
            while queue and queue[0][1] in used:
                queue.popleft()
        
        return True