class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice_creams = 0
        for cost in costs:
            if coins < cost:
                break
            ice_creams += 1
            coins -= cost
        return ice_creams