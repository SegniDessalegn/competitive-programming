class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        def can_plant(i):
            if flowerbed[i] == 1:
                return False
            
            check_left = i - 1 < 0 or flowerbed[i - 1] == 0
            check_right = i + 1 == len(flowerbed) or flowerbed[i + 1] == 0
            
            return check_left and check_right
            
        for i in range(len(flowerbed)):
            if can_plant(i):
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0
    