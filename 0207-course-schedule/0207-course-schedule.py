class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # coloring nodes white, grey and black to find cycles in directed graph
        
        graph = defaultdict(set)
        for p in prerequisites:
            graph[p[0]].add(p[1])
        
        def dfs(i, grey):
            nonlocal black
            ans = True
            for n in graph[i]:
                if n not in black and n not in grey:
                    grey.add(n)
                    ans = ans and dfs(n, grey.copy())
                    if not ans:
                        return False
                    grey.remove(n)
                    black.add(n)
                else:
                    if n in grey:
                        return False
            return ans
        
        black = set()
        for n in range(numCourses):
            if n not in black:
                black.add(n)
                if not dfs(n, set([n])):
                    return False
        
        return True