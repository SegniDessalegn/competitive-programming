class Solution:
    def minimumDistance(self, word: str) -> int:
        
        def get_coordinate(char):
            diff = ord(char) - ord("A")
            return (diff // 6, diff % 6)
        
        def get_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        @cache
        def get_cost(i, f1, f2):
            if i == N:
                return 0
            
            min_cost = float("inf")
            
            curr_cost_f1 = get_distance(f1, get_coordinate(word[i])) if f1 is not None else 0
            min_cost = curr_cost_f1 + get_cost(i + 1, get_coordinate(word[i]), f2)
            
            curr_cost_f2 = get_distance(f2, get_coordinate(word[i])) if f2 is not None else 0
            min_cost = min(min_cost, curr_cost_f2 + get_cost(i + 1, f1, get_coordinate(word[i])))
            
            return min_cost
        
        N = len(word)
        return get_cost(0, None, None)
        