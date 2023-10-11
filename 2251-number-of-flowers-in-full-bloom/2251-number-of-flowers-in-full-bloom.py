class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # sweep line algorithm
        
        START = 0
        END = 1
        time = []
        for start, end in flowers:
            time.append((start, START))
            time.append((end + 1, END))
        
        time.sort()
        
        P = len(people)
        for i in range(P):
            people[i] = (people[i], i)
        
        people.sort()
        
        ptr = 0
        ans = [0] * P
        curr_flowers = 0
        for i in range(len(time)):
            while ptr < P and people[ptr][0] < time[i][0]:
                ans[people[ptr][1]] = curr_flowers
                ptr += 1
            
            if time[i][1] == START:
                curr_flowers += 1
            else:
                curr_flowers -= 1
        
        return ans
    