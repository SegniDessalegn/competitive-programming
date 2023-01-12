class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.ans = [0] * n
        graph = {}
        connected = set([0])
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            if edge[0] in connected:
                graph[edge[0]].append(edge[1])
                connected.add(edge[1])
            else:
                graph[edge[1]].append(edge[0])
                connected.add(edge[0])
        
        self.depth_first_search(graph, labels)
        
        return self.ans
    
    def depth_first_search(self, graph, labels, curr = 0):
        count = {chr(97 + i): 0 for i in range(26)}
        
        for n in graph[curr]:
            new = self.depth_first_search(graph, labels, n)
            for c in count:
                count[c] += new[c]
        
        count[labels[curr]] += 1
        self.ans[curr] = count[labels[curr]]
        
        return count