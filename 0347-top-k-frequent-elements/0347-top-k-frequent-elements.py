class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        for c in count:
            freq[count[c]].append(c)
        
        answer = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                for n in freq[i]:
                    k -= 1
                    answer.append(n)
            if k == 0:
                break
            
        return answer