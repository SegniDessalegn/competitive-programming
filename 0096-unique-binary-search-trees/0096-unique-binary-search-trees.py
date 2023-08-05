class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def backTrack(ns):
            if len(ns) == 0:
                return 1
            
            count = 0
            ns = list(ns)
            for i in range(len(ns)):
                curr_count = backTrack(tuple(ns[:i]))
                curr_count *= backTrack(tuple(ns[i + 1:]))
                count += curr_count
            
            return count
        
        return backTrack(tuple([i + 1 for i in range(n)]))
