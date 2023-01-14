class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        relation = defaultdict(set)
        for a, b in zip(s1, s2):
            relation[a].add(b)
            relation[b].add(a)
        
        smallest = ""
        for char in baseStr:
            stack = [char]
            visited = set()
            min_char = char
            while stack:
                curr = stack.pop()
                min_char = min(min_char, curr)
                for c in relation[curr]:
                    if c not in visited:
                        stack.append(c)
                        visited.add(c)
            smallest += min_char
        
        return smallest