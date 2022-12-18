class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([("0000", 0)])
        visited = set("0000")
        if "0000" in deadends:
            return -1
        while queue:
            curr, turns = queue.popleft()
            if curr == target:
                return turns
            for i in range(len(curr)):
                if curr[i] != "9":
                    code = curr[:i] + str(int(curr[i]) + 1) + curr[i + 1:]
                else:
                    code = curr[:i] + "0" + curr[i + 1:]
                if code not in visited and code not in deadends:
                    queue.append((code, turns + 1))
                    visited.add(code)
                if curr[i] != "0":
                    code = curr[:i] + str(int(curr[i]) - 1) + curr[i + 1:]
                else:
                    code = curr[:i] + "9" + curr[i + 1:]
                if code not in visited and code not in deadends:
                    queue.append((code, turns + 1))
                    visited.add(code)
        return -1