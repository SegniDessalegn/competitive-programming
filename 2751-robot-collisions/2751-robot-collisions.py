class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robot = []
        for i in range(len(positions)):
            robot.append([positions[i], healths[i], directions[i], i])
        
        robot.sort()
        
        stack = []
        for i in range(len(robot)):
            if robot[i][2] == "R":
                stack.append(robot[i])
            else:
                can_append = True
                while stack and stack[-1][2] == "R":
                    popped = stack.pop()
                    if popped[1] > robot[i][1]:
                        popped[1] -= 1
                        stack.append(popped)
                        can_append = False
                        break
                    elif popped[1] == robot[i][1]:
                        can_append = False
                        break
                    robot[i][1] -= 1
                if can_append:
                    stack.append(robot[i])
        
        ans = [-1] * len(positions)
        for robot in stack:
            ans[robot[3]] = robot[1]
        
        real_ans = []
        for pos in ans:
            if pos != -1:
                real_ans.append(pos)
        
        return real_ans