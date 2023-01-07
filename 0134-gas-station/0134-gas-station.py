class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        original_length = len(gas)
        left = 0
        right = 0
        curr_tank = 0
        while right < len(gas):
            # at each step, the car's gas tank icrements by gas[right] - cost[right]
            curr_tank += gas[right] - cost[right]
            
            # if curr_tank is less than zero, move the left pointer until curr_tank becomes non negative
            while curr_tank < 0:
                curr_tank += cost[left] - gas[left]
                left += 1
            
            # if the length of current window is equal to the original length of gas, then return left (starting index)
            if right - left + 1 == original_length:
                return left
            
            # since the motion of the car is circular, we have to append the gas and cost elements to the end of the lists to account for that
            if len(gas) < 2 * original_length:
                gas.append(gas[right])
                cost.append(cost[right])
            
            right += 1
        
        return -1