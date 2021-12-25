class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        three = n // 3
        five = n // 5
        output = [str(i + 1) for i in range(n)]

        if n >= 3:
            index = 2
            while index < n:
                output[index] = "Fizz"
                index += 3

        if n >= 5:
            index = 4
            while index < n:
                if output[index] == "Fizz":
                    output[index] += "Buzz"
                else:
                    output[index] = "Buzz"
                index += 5
        return output


