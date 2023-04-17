class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(1, len(parent)):
            graph[parent[i]].append(i)
        
        def traverse(node):
            nonlocal max_path
            paths = [0, 0]
            for n in graph[node]:
                if s[node] is not s[n]:
                    paths.append(1 + traverse(n))
                else:
                    traverse(n)
            paths.sort()
            max_path = max(max_path, paths[-1] + paths[-2] + 1)
            return paths[-1]
        
        max_path = 1
        traverse(0)
        return max_path