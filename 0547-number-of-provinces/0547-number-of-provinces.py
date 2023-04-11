class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        visited = set()
        for city in isConnected:
            for c in range(len(city)):
                if c not in visited and city[c] == 1:
                    stack = [c]
                    visited.add(c)
                    while stack:
                        curr = stack.pop()
                        for i in range(len(isConnected[curr])):
                            if i not in visited and isConnected[curr][i] == 1:
                                stack.append(i)
                                visited.add(i)
                    province += 1
        return province