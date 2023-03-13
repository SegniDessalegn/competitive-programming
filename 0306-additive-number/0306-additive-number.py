class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def recur(num = num, curr_ans = []):
            if not num:
                # this is the place where we check for validity of every possible sequence
                return check(curr_ans) and len(curr_ans) >= 3
                
            for i in range(len(num)):
                curr_ans.append(num[:i + 1])
                # pruning, if the current answer is invalid, we don't have to search anymore
                if check(curr_ans):
                    # if we can find the answer once, we can return it to the parent call, there is no need to search anymore
                    if recur(num[i + 1:], curr_ans):
                        return True
                curr_ans.pop()
        
        
        # checks whether a sequence is additive sequence or not
        def check(sequence):
            for i in range(2, len(sequence)):
                if sequence[i][0] == "0" and len(sequence[i]) > 1:
                    return False
                if int(sequence[i - 2]) + int(sequence[i - 1]) != int(sequence[i]):
                    return False
            
            if len(sequence[0]) > 1 and sequence[0][0] == "0":
                return False
            if len(sequence) > 1 and len(sequence[1]) > 1 and sequence[1][0] == "0":
                return False
            
            return True
        
        return recur()
