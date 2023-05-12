class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        
        answer = []
        for i in range(len(quiet)):
            stack = [i]
            visited = set([i])
            quietest = quiet[i]
            person = i
            while stack:
                curr = stack.pop()
                if quiet[curr] < quietest:
                    quietest = quiet[curr]
                    person = curr
                
                for n in graph[curr]:
                    if n not in visited:
                        stack.append(n)
                        visited.add(n)
            
            answer.append(person)
        
        return answer