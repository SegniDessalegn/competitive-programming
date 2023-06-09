class Solution:
    def candy(self, ratings: List[int]) -> int:
        right = self.count(ratings, False)
        left = self.count(ratings[::-1], True)
        return self.get_candies(right, left) + len(ratings)
    
    def count(self, arr, reverse):
        i = 1
        n = len(arr)
        peaks = {}
        while i < n:
            length = 0
            start = i - 1
            while i < n and arr[i] < arr[i - 1]:
                i += 1
                length += 1
            if not reverse:
                peaks[start] = length
            else:
                peaks[n - start - 1] = length
            i += 1
        
        return peaks
    
    def get_candies(self, right, left):
        candies = 0
        for i in right:
            if i in left:
                if right[i] > left[i]:
                    candies += self.calculate(right[i])
                    candies += self.calculate(left[i] - 1)
                else:
                    candies += self.calculate(left[i])
                    candies += self.calculate(right[i] - 1)
            else:
                candies += self.calculate(right[i])
        
        for i in left:
            if i not in right:
                candies += self.calculate(left[i])
        
        return candies
            
    
    def calculate(self, n):
        return (n * (n + 1)) // 2