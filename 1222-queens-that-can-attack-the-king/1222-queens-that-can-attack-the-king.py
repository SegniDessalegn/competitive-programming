class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        pos = []
        queens_pos = set()
        for cord in queens:
            queens_pos.add(tuple(cord))
        
        directions = [[1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1], [0, 1], [0, -1]]
        for curr_direction in directions:
            curr_pos = king[:]
            while 0 <= curr_pos[0] < 8 and 0 <= curr_pos[1] <= 8:
                if tuple(curr_pos) in queens_pos:
                    pos.append(curr_pos[:])
                    break
                curr_pos[0] += curr_direction[0]
                curr_pos[1] += curr_direction[1]
        return pos