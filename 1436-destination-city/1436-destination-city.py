class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        keys = set([path[0] for path in paths])
        vals = set([path[1] for path in paths])
        
        for city in vals:
            if city not in keys:
                return city
        
        assert(False)
