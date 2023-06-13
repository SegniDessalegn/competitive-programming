class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        dist1 = 0
        dist2 = 0
        for i in range(len(word1)):
            index = ord(word1[i]) - 97
            if count1[index] == 0:
                dist1 += 1
            count1[index] += 1
        
        for i in range(len(word2)):
            index = ord(word2[i]) - 97
            if count2[index] == 0:
                dist2 += 1
            count2[index] += 1
        
        for i in range(26):
            for j in range(26):
                c1 = count1[i]
                c2 = count2[j]
                if c1 > 0 and c2 > 0:
                    count1[i] -= 1
                    count1[ord(chr(j + 97)) - 97] += 1
                    count2[j] -= 1
                    count2[ord(chr(i + 97)) - 97] += 1
                    
                    if self.is_valid(count1, count2):
                        return True
                    
                    count1[i] += 1
                    count1[ord(chr(j + 97)) - 97] -= 1
                    count2[j] += 1
                    count2[ord(chr(i + 97)) - 97] -= 1
        
        return False
    
    
    def is_valid(self, count1, count2):
        dist1 = 0
        dist2 = 0
        for c1 in count1:
            if c1 > 0:
                dist1 += 1
        for c2 in count2:
            if c2 > 0:
                dist2 += 1
        
        return dist1 == dist2