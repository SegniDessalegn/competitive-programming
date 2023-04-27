class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        queue = deque([("0000", 0)])
        visited = set("0000")
        while queue:
            curr, turns = queue.popleft()
            if curr == target:
                return turns
            for i in range(4):
                turn1 = curr[:i] + nums[(int(curr[i]) + 1) % 10] + curr[i + 1:]
                if turn1 not in visited and turn1 not in deadends:
                    queue.append((turn1, turns + 1))
                    visited.add(turn1)
                turn2_index = int(curr[i]) - 1
                if turn2_index == -1:
                    turn2_index = 9
                turn2 = curr[:i] + nums[turn2_index] + curr[i + 1:]
                if turn2 not in visited and turn2 not in deadends:
                    queue.append((turn2, turns + 1))
                    visited.add(turn2)
        return -1