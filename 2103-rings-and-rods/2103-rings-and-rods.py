class Solution:
    def countPoints(self, rings: str) -> int:
        contents = {}
        for i in range(1, len(rings), 2):
            contents[rings[i]] = contents.get(rings[i], set())
            contents[rings[i]].add(rings[i - 1])
        
        count = 0
        for content in contents.values():
            if len(content) == 3:
                count += 1
        
        return count