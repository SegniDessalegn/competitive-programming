class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        squares = set()
        for i in range(10 ** 5):
            squares.add(i * i)
        
        @cache
        def find_ans(mask, prev):
            if mask == (1 << N) - 1:
                return 1
            
            count = 0
            for i in range(len(nums)):
                if (mask & (1 << i)) == 0 and (prev == -1 or nums[i] + nums[prev] in squares):
                    count += find_ans(mask | (1 << i), i)
            
            return count
        
        N = len(nums)
        result = find_ans(0, -1)
        
        permutations = [1] * 13
        for i in range(2, 13):
            permutations[i] = permutations[i - 1] * i
        
        count = Counter(nums)
        for c in count:
            result //= permutations[count[c]]
        
        return result
    