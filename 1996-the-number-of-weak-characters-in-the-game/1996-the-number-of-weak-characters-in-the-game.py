class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        N = len(properties)
        
        properties.sort()
        
        max_nums = [properties[-1][1]]
        for i in range(N - 2, -1, -1):
            max_nums.append(max(max_nums[-1], properties[i][1]))
        max_nums = max_nums[::-1]
        
        start = [a for a, b in properties]
        count = 0
        for a, b in properties:
            idx = bisect_left(start, a + 1)
            if idx < N and max_nums[idx] > b:
                count += 1
        
        return count