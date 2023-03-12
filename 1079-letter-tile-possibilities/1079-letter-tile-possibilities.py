class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        solutions = set()
        def recur(tiles, curr_ans = []):
            for i in range(len(tiles)):
                curr_ans.append(tiles[i])
                solutions.add(tuple(curr_ans))
                recur(tiles[:i] + tiles[i + 1:], curr_ans)
                curr_ans.pop()
        
        recur(tiles)
        return len(solutions)