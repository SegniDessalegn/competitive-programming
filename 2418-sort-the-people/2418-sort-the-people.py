class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for _ in range(len(names)):
            i = 1
            swapped = False
            while i < len(names):
                if heights[i] > heights[i - 1]:
                    heights[i], heights[i - 1] = heights[i - 1], heights[i]
                    names[i], names[i - 1] = names[i - 1], names[i]
                    swapped = True
                i += 1
            if not swapped:
                break
        
        return names