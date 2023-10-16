class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairs_graph = defaultdict(int)
        for a, b in pairs:
            pairs_graph[a] = b
            pairs_graph[b] = a
        
        for i in range(n):
            preferences[i] = {preferences[i][j]: j for j in range(n - 1)}
        
        unhappy = 0
        for pair in pairs:
            for a in pair:
                for friend in preferences[a]:
                    if preferences[a][friend] < preferences[a][pairs_graph[a]] and preferences[friend][a] < preferences[friend][pairs_graph[friend]]:
                        unhappy += 1
                        break
        
        return unhappy
    