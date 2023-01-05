class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # separate into real and imaginary part for num1
        real = num1[:num1.find("+")]
        imaginary = num1[num1.find("+") + 1:]
        
        # multiply real and imaginary part of num1 with num2
        mult1 = self.multiply(real, num2)
        mult2 = self.multiply(imaginary, num2)

        # add the multiplications together
        ans = self.add(mult1, mult2)
        
        return ans

    def multiply(self, m, n):
        # we can do the multiplication based on whether m is real or imaginary
        if m[-1] == "i":
            real = str(-1 * int(m[:len(m) - 1]) * int(n[n.find("+") + 1:len(n) -1]))
            imaginary = str(int(m[:len(m) - 1]) * int(n[:n.find("+")])) + "i"
        else:
            real = str(int(m) * int(n[:n.find("+")]))
            imaginary = str(int(m) * int(n[n.find("+") + 1:len(n) - 1])) + "i"
        
        return real + "+" + imaginary

    def add(self, m, n):
        # add real parts and imaginarys part together
        real = str(int(m[:m.find("+")]) + int(n[:n.find("+")]))
        imaginary = str(int(m[m.find("+") + 1:len(m) - 1]) + int(n[n.find("+") + 1:len(n) - 1])) + "i"
        
        return real + "+" + imaginary