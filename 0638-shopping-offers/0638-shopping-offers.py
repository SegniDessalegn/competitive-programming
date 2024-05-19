class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        @cache
        def get_ans(needs):
            if min(needs) < 0:
                return float("inf")
            
            cost = 0
            for i in range(P):
                cost += price[i] * needs[i]
            
            for i in range(S):
                special_cost = special[i][-1]
                temp = []
                for j in range(P):
                    temp.append(needs[j] - special[i][j])
                
                cost = min(cost, special_cost + get_ans(tuple(temp)))
            
            return cost
        
        
        P = len(price)
        S = len(special)
        
        return get_ans(tuple(needs))
    