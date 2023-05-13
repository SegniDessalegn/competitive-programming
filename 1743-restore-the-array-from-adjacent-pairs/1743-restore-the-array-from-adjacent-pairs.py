class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        degree = defaultdict(int)
        for edge in adjacentPairs:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        
        n = len(graph)
        queue = deque()
        side = 0
        l, r = 0, n - 1
        ans = [None for _ in range(n)]
        for num in graph:
            if degree[num] == 1:
                queue.append((num, side))
                if side == 0:
                    ans[l] = num
                    l += 1
                else:
                    ans[r] = num
                    r -= 1
                side += 1
        
        while queue:
            length = len(queue)
            for _ in range(length):
                curr, side = queue.popleft()
                for neighbour in graph[curr]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        queue.append((neighbour, side))
                        if side == 0:
                            ans[l] = neighbour
                            l += 1
                        else:
                            ans[r] = neighbour
                            r -= 1
        
        return ans
    