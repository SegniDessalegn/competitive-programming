class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(node, target, visited, curr_ans = 1):
            nonlocal graph
            if node == target:
                return curr_ans
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    curr_ans *= n[1]
                    val = dfs(n[0], target, visited.copy(), curr_ans)
                    if val is not None:
                        return val
                    visited.remove(n)
                    curr_ans /= n[1]
            
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        answers = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                answers.append(-1)
                continue
            val = dfs(q[0], q[1], set([q[0]]))
            if val is None:
                val = -1
            answers.append(val)
            
        return answers