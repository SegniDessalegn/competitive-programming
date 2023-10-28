class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        @cache
        def get_ans(char, n):
            if n == 0:
                return 1
            
            curr_count = 0
            
            if char == "a":
                curr_count += get_ans("e", n - 1)
            elif char == "e":
                curr_count += get_ans("a", n - 1) + get_ans("i", n - 1)
            elif char == "i":
                for next_char in "aeou":
                    curr_count += get_ans(next_char, n - 1)
            elif char == "o":
                curr_count += get_ans("i", n - 1) + get_ans("u", n - 1)
            elif char == "u":
                curr_count += get_ans("a", n - 1)
            
            return curr_count % MOD
        
        
        MOD = 10 ** 9 + 7
        count = 0
        for char in "aeiou":
            count += get_ans(char, n - 1)
            count %= MOD
        
        return count
    