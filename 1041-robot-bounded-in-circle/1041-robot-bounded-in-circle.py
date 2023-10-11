class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        def update_pos(position, curr_direction):
            return (position[0] + curr_direction[0], position[1] + curr_direction[1])
        
        def update_dir(curr_direction, next_direction):
            if curr_direction == NORTH:
                if next_direction == "L":
                    return WEST
                else:
                    return EAST
            elif curr_direction == SOUTH:
                if next_direction == "L":
                    return EAST
                else:
                    return WEST
            elif curr_direction == EAST:
                if next_direction == "L":
                    return NORTH
                else:
                    return SOUTH
            else:
                if next_direction == "L":
                    return SOUTH
                else:
                    return NORTH
        
        NORTH = (-1, 0)
        SOUTH = (1, 0)
        EAST = (0, 1)
        WEST = (0, -1)
        curr_direction = NORTH
        curr_position = (0, 0)
        
        for _ in range(4):
            for instruction in instructions:
                if instruction == "G":
                    curr_position = update_pos(curr_position, curr_direction)
                else:
                    curr_direction = update_dir(curr_direction, instruction)

            if curr_position == (0, 0):
                return True
        
        return False