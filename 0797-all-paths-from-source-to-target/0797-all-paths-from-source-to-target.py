class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.dfs(graph, 0, [0], [])

    def dfs(self, graph, i, curr_path, ans):
        if i == len(graph) - 1:
            ans.append(curr_path[:])
            return ans
        for node in graph[i]:
            curr_path.append(node)
            self.dfs(graph, node, curr_path, ans)
            curr_path.pop()
        return ans