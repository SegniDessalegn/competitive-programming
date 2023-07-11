class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # topological sorting
        
        row_relation = defaultdict(list)
        row_indegree = defaultdict(int)
        for a, b in rowConditions:
            row_relation[a].append(b)
            row_indegree[b] += 1
        
        col_relation = defaultdict(list)
        col_indegree = defaultdict(int)
        for a, b in colConditions:
            col_relation[a].append(b)
            col_indegree[b] += 1
        
        # fill rows
        row_pos = {}
        queue = deque()
        for i in range(1, k + 1):
            if row_indegree[i] == 0:
                queue.append(i)
        
        index = 0
        while queue:
            curr = queue.popleft()
            row_pos[curr] = index
            index += 1
            for neighbour in row_relation[curr]:
                row_indegree[neighbour] -= 1
                if row_indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if index != k:
            return []
        
        # fill column
        col_pos = {}
        queue = deque()
        for i in range(1, k + 1):
            if col_indegree[i] == 0:
                queue.append(i)
        
        index = 0
        while queue:
            curr = queue.popleft()
            col_pos[curr] = index
            index += 1
            for neighbour in col_relation[curr]:
                col_indegree[neighbour] -= 1
                if col_indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if index != k:
            return []
        
        mat = [[0 for _ in range(k)] for __ in range(k)]
        for i in range(1, k + 1):
            mat[row_pos[i]][col_pos[i]] = i
        
        return mat