class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        def count_to_pal(s):
            left = 0
            right = len(s) - 1
            count = 0
            while left < right:
                if s[left] != s[right]:
                    count += 1
                left += 1
                right -= 1
            return count
        
        @cache
        def get(start, end, curr_k):
            if end == N:
                if start == N and curr_k == 0:
                    return 0
                return float("inf")
            if k == 0:
                return float("inf")
            
            # choose
            count = count_to_pal(s[start:end+1]) + get(end + 1, end + 1, curr_k - 1)
            
            # do not choose
            count = min(count, get(start, end + 1, curr_k))
            
            return count
        
        N = len(s)
        return get(0, 0, k)