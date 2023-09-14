class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        nums.append(float("inf"))
        N = len(nums)
        valid = [False] * N
        for i in range(N):
            if minK <= nums[i] <= maxK:
                valid[i] = True
        
        min_found = False
        max_found = False
        for i in range(N):
            if nums[i] == minK:
                min_found = True
            if nums[i] == maxK:
                max_found = True
            
            if not valid[i]:
                if not (min_found and max_found):
                    for j in range(i - 1, -1, -1):
                        if not valid[j]:
                            break
                        valid[j] = False
                min_found = False
                max_found = False
        
        ans = 0
        i = 0
        while i < N:
            min_index = deque([])
            max_index = deque([])
            prev = i
            length = 0
            while i < N and valid[i]:
                if nums[i] == minK:
                    min_index.append(i)
                if nums[i] == maxK:
                    max_index.append(i)
                length += 1
                i += 1
            
            if minK == maxK:
                ans += (length * (length + 1)) // 2
                i += 1
                continue
            
            j = prev
            curr_ans = 0
            while j < i and min_index and max_index:
                end = max(min_index[0], max_index[0])
                curr_ans += (i - end)
                if j == min_index[0]:
                    min_index.popleft()
                if j == max_index[0]:
                    max_index.popleft()
                j += 1
            
            ans += curr_ans
            i += 1
        
        return ans