class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # topological sort
        
        graph = {}
        for recipe in recipes:
            graph[recipe] = []
        for supply in supplies:
            graph[supply] = []
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                graph[ingredient] = []
        
        indegree = {g:0 for g in graph}
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                indegree[recipes[i]] += 1
        
        queue = deque()
        for recipe in indegree:
            if indegree[recipe] == 0:
                queue.append(recipe)
        
        recipes = set(recipes)
        supplies = set(supplies)
        ans = []
        while queue:
            curr = queue.pop()
            if curr not in recipes and curr not in supplies:
                continue
            if curr in recipes:
                ans.append(curr)
            for neighbour in graph[curr]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return ans