class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pref = [0]
        for c in customers:
            if c == "Y":
                pref.append(pref[-1] + 1)
            else:
                pref.append(pref[-1])
        
        suff = [0]
        for c in customers[::-1]:
            if c == "Y":
                suff.append(suff[-1] + 1)
            else:
                suff.append(suff[-1])
        suff = suff[::-1]
        
        penality = len(customers)
        time = len(customers)
        for i in range(len(customers)):
            curr_penality = suff[i] + i - pref[i]
            if curr_penality < penality:
                penality = curr_penality
                time = i
        
        if len(customers) - pref[-1] < penality:
            time = len(customers)
        
        return time