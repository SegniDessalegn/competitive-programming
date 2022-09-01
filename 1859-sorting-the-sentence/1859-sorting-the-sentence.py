class Solution:
    def sortSentence(self, s: str) -> str:
        spaces = 0
        for i in s:
            if i == " ":
                spaces += 1
        last_space = 0
        words = [None for i in range(spaces + 1)]
        for i in range(len(s)):
            if 48 <= ord(s[i]) <= 57:
                current_word = s[last_space : i]
                if int(s[i]) != 1:
                    current_word = " " + current_word
                last_space = i + 2
                words[int(s[i]) - 1] = current_word
                if last_space >= len(s):
                    break
        sentence = ""
        for i in words:
            sentence += i
        return sentence
                