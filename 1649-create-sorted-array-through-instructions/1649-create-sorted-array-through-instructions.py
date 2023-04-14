class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def merge_sort(i, j):
            if i == j:
                return [instructions[i]]
            mid = (i + j) // 2
            left = merge_sort(i, mid)
            right = merge_sort(mid + 1, j)
            
            left_length = len(left)
            right_length = len(right)
            left_count = defaultdict(int)
            for n in left:
                left_count[n[0]] += 1
            sorted_nums = []
            l = 0
            r = 0
            while l < left_length and r < right_length:
                if left[l][0] < right[r][0]:
                    sorted_nums.append(left[l])
                    l += 1
                else:
                    less_greater[right[r][1]][0] += l
                    less_greater[right[r][1]][1] += left_length - l - left_count[right[r][0]]
                    sorted_nums.append(right[r])
                    r += 1
            while l < left_length:
                sorted_nums.append(left[l])
                l += 1
            while r < right_length:
                less_greater[right[r][1]][0] += l
                less_greater[right[r][1]][1] += left_length - l - left_count[right[r][0]]
                sorted_nums.append(right[r])
                r += 1
            return sorted_nums
        
        for i in range(len(instructions)):
            instructions[i] = (instructions[i], i)
        
        less_greater = {i:[0, 0] for i in range(len(instructions))}
        merge_sort(0, len(instructions) - 1)
        total_cost = 0
        for n in less_greater:
            total_cost += min(less_greater[n][0], less_greater[n][1])
        
        return total_cost % (10 ** 9 + 7)