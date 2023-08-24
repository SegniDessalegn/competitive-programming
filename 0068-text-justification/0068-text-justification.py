class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        N = len(words)
        ans = []
        index = 0
        while index < N:
            total_length = 0
            j = 0
            curr_words = []
            while index < N and total_length + j + len(words[index]) <= maxWidth:
                total_length += len(words[index])
                curr_words.append(words[index])
                index += 1
                j += 1
            
            left = maxWidth - total_length
            if len(curr_words) != 1:
                space = left // (len(curr_words) - 1)
                left_spaces = left % (len(curr_words) - 1)
                spaces = []
                for i in range(len(curr_words) - 1):
                    if left_spaces > 0:
                        spaces.append(" " * (space + 1))
                        left_spaces -= 1
                    else:
                        spaces.append(" " * space)
            
                curr_ans = []
                for i in range(len(curr_words)):
                    curr_ans.append(curr_words[i])
                    if i != len(curr_words) - 1:
                        curr_ans.append(spaces[i])
            else:
                curr_ans = [curr_words[0]]
                curr_ans.append(" " * (maxWidth - len(curr_words[0])))
            
            ans.append("".join(curr_ans))
        
        last_line = ans[-1]
        new_last_line = []
        can_insert = True
        for i in range(len(last_line)):
            if last_line[i] == " ":
                if can_insert:
                    new_last_line.append(last_line[i])
                    can_insert = False
            else:
                new_last_line.append(last_line[i])
                can_insert = True
        length = len(new_last_line)
        for i in range(maxWidth - length):
            new_last_line.append(" ")
        
        ans[-1] = "".join(new_last_line)
        
        return ans