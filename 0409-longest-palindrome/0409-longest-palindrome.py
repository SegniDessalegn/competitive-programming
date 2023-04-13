class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        odds = []
        count = Counter(s)
        for c in count:
            if count[c] % 2 == 0:
                length += count[c]
            else:
                odds.append(count[c])
        
        odds.sort(reverse = True)
        
        for i in range(len(odds)):
            if odds[i] == 1:
                length += 1
                break
            else:
                if i == len(odds) - 1:
                    length += odds[i]
                else:
                    length += (odds[i] // 2) * 2
        
        return length