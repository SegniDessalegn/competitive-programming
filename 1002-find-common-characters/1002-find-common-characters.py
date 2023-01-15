class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = []
        for word in words:
            curr_count = [0] * 26
            for char in word:
                curr_count[ord(char) - 97] += 1
            count.append(curr_count)
        
        common = []
        for j in range(26):
            min_count = count[0][j]
            for i in range(len(words)):
                min_count = min(min_count, count[i][j])
            for _ in range(min_count):
                common.append(chr(j + 97))
        
        return common