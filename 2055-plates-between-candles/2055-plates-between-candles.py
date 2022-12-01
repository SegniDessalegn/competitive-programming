class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [0]
        for char in s:
            if char == "|":
                candles.append(candles[-1] + 1)
            else:
                candles.append(candles[-1])
        plates = []
        for q in queries:
            left, right = q[0] + 1, q[1] + 1
            if candles[left - 1] == candles[left]:
                while left <= right:
                    index = (left + right) // 2
                    if candles[index] == candles[q[0] + 1]:
                        left = index + 1
                    else:
                        right = index - 1
                start = max(left, right)
            else:
                start = left
            left, right = q[0] + 1, q[1] + 1
            if candles[right - 1] >= candles[right]:
                while left <= right:
                    index = (left + right) // 2
                    if candles[index] == candles[q[1] + 1]:
                        right = index - 1
                    else:
                        left = index + 1
            end = max(left, right)
            if start <= end:
                plates.append(end - start + 1 - (candles[end] - candles[start] + 1))
            else:
                plates.append(0)
        return plates