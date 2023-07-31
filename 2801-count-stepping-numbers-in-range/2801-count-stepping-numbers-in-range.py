class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        
        @cache
        def recur(can_choose, is_first, prev_digit, index, s):
            if index == len(s):
                return 1
            
            if can_choose:
                limit = 10
            else:
                limit = int(s[index]) + 1
            ans = 0
            for i in range(0, limit):
                if not is_first and abs(prev_digit - i) != 1:
                    continue
                
                new_can_choose = can_choose or i != limit - 1
                new_is_first = is_first
                if new_is_first:
                    if i != 0:
                        new_is_first = False
                ans += recur(new_can_choose, new_is_first, i, index + 1, s)
            
            return ans % (10 ** 9 + 7)
        
        high_count = recur(False, True, 0, 0, high)
        
        low = str(int(low) - 1)
        low_count = recur(False, True, 0, 0, low)
        
        return (high_count - low_count) % (10 ** 9 + 7)