class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for n in nums:
            if n > 0:
                positives.append(n)
            else:
                negatives.append(n)
        
        rearranged = []
        for i in range(len(positives)):
            rearranged.append(positives[i])
            rearranged.append(negatives[i])
        
        return rearranged