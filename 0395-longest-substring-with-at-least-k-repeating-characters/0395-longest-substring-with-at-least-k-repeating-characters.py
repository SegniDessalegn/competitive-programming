class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        N = len(s)
        ans = 0
        
        # brute force over the number of unique characters
        for unique in range(1, 27):
            curr_count = defaultdict(int)
            left = 0
            for right in range(N):
                curr_count[s[right]] += 1
                while len(curr_count) > unique:
                    curr_count[s[left]] -= 1
                    if curr_count[s[left]] == 0:
                        curr_count.pop(s[left])
                    left += 1
                
                valid = True
                for count in curr_count.values():
                    if count < k:
                        valid = False
                        break
                
                if valid:
                    ans = max(ans, right - left + 1)
        
        return ans