class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # find which numbers should be positioned at even and odd index
        
        N = len(nums)
        if N == 1:
            return 0
        
        odd_count = defaultdict(int)
        even_count = defaultdict(int)
        
        for i in range(N):
            if i % 2 == 0:
                even_count[nums[i]] += 1
            else:
                odd_count[nums[i]] += 1
        
        odd_count_arr = []
        for num in odd_count:
            odd_count_arr.append((odd_count[num], num))
        
        even_count_arr = []
        for num in even_count:
            even_count_arr.append((even_count[num], num))
        
        odd_count_arr.sort(reverse = True)
        even_count_arr.sort(reverse = True)
        
        if even_count_arr[0][1] == odd_count_arr[0][1]:
            if len(odd_count) == len(even_count) == 1:
                return N // 2
            elif len(odd_count) == 1:
                return min(self.get_ops(nums, even_count_arr[0][1], even_count_arr[1][1]), self.get_ops(nums, even_count_arr[1][1], even_count_arr[0][1]))
            elif len(even_count) == 1:
                return min(self.get_ops(nums, odd_count_arr[0][1], odd_count_arr[1][1]), self.get_ops(nums, odd_count_arr[1][1], odd_count_arr[0][1]))
            elif even_count_arr[1][0] + odd_count_arr[0][0] > even_count_arr[0][0] + odd_count_arr[1][0]:
                return self.get_ops(nums, even_count_arr[1][1], odd_count_arr[0][1])
            else:
                return self.get_ops(nums, even_count_arr[0][1], odd_count_arr[1][1])
        
        return self.get_ops(nums, even_count_arr[0][1], odd_count_arr[0][1])
    
    
    def get_ops(self, nums, even_num, odd_num):
        ops = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ops += nums[i] != even_num
            else:
                ops += nums[i] != odd_num
        
        return ops
    