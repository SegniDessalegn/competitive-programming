class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def back_track(i, curr):
            nonlocal ans
            ans = max(ans, check(curr))
            for j in range(i, len(words)):
                curr.append(words[j])
                back_track(j + 1, curr.copy())
                curr.pop()
        
        def check(arr):
            s = "".join(arr)
            s_count = Counter(s)
            curr_ans = 0
            for char in s_count:
                if char not in count or count[char] < s_count[char]:
                    return 0
                curr_ans += s_count[char] * score[ord(char) - 97]
            
            return curr_ans
        
        ans = 0
        count = Counter(letters)
        back_track(0, [])
        
        return ans
            