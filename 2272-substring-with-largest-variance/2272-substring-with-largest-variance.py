class Solution:
    def largestVariance(self, s: str) -> int:
        N = len(s)
        chars = [chr(i) for i in range(97, 97 + 26)]
        count = Counter(s)
        
        # kadane's algorithm
        # treat the smaller character as -1
        # treat the larger character as +1
        max_sum = 0
        for min_char in chars:
            for max_char in chars:
                if min_char == max_char:
                    continue
                
                min_count = 0
                max_count = 0
                min_left_count = count[min_char]
                for char in s:
                    if char == max_char:
                        max_count += 1
                    elif char == min_char:
                        min_count += 1
                        min_left_count -= 1
                    
                    if min_count > 0:
                        max_sum = max(max_sum, max_count - min_count)
                    
                    if max_count < min_count and min_left_count > 0:
                        min_count = 0
                        max_count = 0
        
        return max_sum