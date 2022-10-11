class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        basket1 = 0
        basket2 = 0
        counter = 0
        start = 0
        results = []
        stop = False
        end = False
        second_counter = 0
        
        while True:
            basket1 = fruits[start]
            for i in range(start, len(fruits)):
                if not stop and not end:
                    if fruits[i] == basket1:
                        counter += 1
                        if i == len(fruits) - 1:
                            end = True
                    else:
                        start = i - 1
                        basket2 = fruits[i]
                        for j in range(i,len(fruits)):
                            if fruits[j] == basket2 or fruits[j] == basket1:
                                counter += 1
                                second_counter += 1
                            elif fruits[j] != basket2 and fruits[j] != basket1:
                                reverse = fruits[j]
                                start = j - second_counter
                                stop = True
                                break
                            if j == len(fruits) - 1:
                                end = True
                                break
                else:
                    stop = False
                    break
            results.append(counter)
            if start + second_counter == len(fruits) - 1 or end:
                break
            counter = 0
            second_counter = 0
        
        large = 0
        for i in range(len(results)):
            if results[i] > large:
                large = results[i]
        return large