class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def is_valid(state):
            for i in range(len(state)):
                if state[i][0] != state[i][1]:
                    return False
            return True
        
        N = len(s)
        left = 0
        right = 0
        max_length = 0
        for i in range(N):
            r = ord("z") - ord("A")
            curr_state = [[False, False] for _ in range(26)]
            for j in range(i, N):
                if s[j].islower():
                    curr_state[ord(s[j].lower()) - 97][0] = True
                else:
                    curr_state[ord(s[j].lower()) - 97][1] = True
                
                if is_valid(curr_state) and j - i + 1 > max_length:
                    left = i
                    right = j
                    max_length = j - i + 1

        return s[left:right + 1] if right != left else ""
            