class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def backtrack(i, open_bracket, removed, curr):
            nonlocal minimum_removal, ans, visited
            
            if removed > minimum_removal:
                return

            if i == len(s):
                if open_bracket == 0 and removed != len(s):
                    if removed < minimum_removal:
                        ans = set(["".join(curr[:])])
                        minimum_removal = removed
                    elif removed == minimum_removal:
                        ans.add("".join(curr[:]))
                return

            current_state = (i, removed, open_bracket, "".join(curr))
            if current_state in visited:
                return
            visited.add(current_state)

            char = s[i]

            if char == "(":
                curr.append(char)
                backtrack(i + 1, open_bracket + 1, removed, curr)
                curr.pop()
            elif char == ")":
                if open_bracket > 0:
                    curr.append(char)
                    backtrack(i + 1, open_bracket - 1, removed, curr)
                    curr.pop()
            else:
                curr.append(char)
                backtrack(i + 1, open_bracket, removed, curr)
                curr.pop()

            if char == "(" or char == ")":
                backtrack(i + 1, open_bracket, removed + 1, curr)

        
        minimum_removal = float("inf")
        ans = set()
        visited = set()
        backtrack(0, 0, 0, [])
        
        return list(ans) if ans else [""]
    