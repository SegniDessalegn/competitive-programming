class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = deque(senate)
        turn = None
        turn_count = 0
        while True:
            length = len(senate)
            if length == 1:
                break
            
            turn_not_changed = True
            for i in range(length):
                curr = senate.popleft()
                if curr == turn:
                    turn_count += 1
                    senate.append(curr)
                else:
                    if turn == None:
                        turn = curr
                        senate.append(curr)
                        turn_count = 1
                    else:
                        turn_count -= 1
                        if turn_count == 0:
                            turn = None
                            turn_not_changed = False
            
            if turn_not_changed:
                break
        
        return "Radiant" if senate[0] == "R" else "Dire"
