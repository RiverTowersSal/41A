"""ones = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M"]"""

class Roman:
    def __init__(self,variable):
        self.ones = tuple(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"])
        self.tens = tuple(["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"])
        self.hundreds = tuple(["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M"])
        self.variable = variable
        self.convert()
        
            def convert(self):
        self.res = ''
        if (self.variable // 100 != 0):
            self.res = self.res + self.hundreds[self.variable // 100 - 1]
        if ((self.variable % 100) // 10 != 0):
            self.res = self.res + self.tens[(self.variable % 100)// 10 - 1]
        if ((self.variable % 10) != 0):
            self.res = self.res + self.ones[self.variable % 10 - 1]

        return self.res

    def __str__(self):
        return self.res
variable = int(input("Enter a integer between 1 and 1000: "))
R = Roman(variable)
print("Variable input:", variable, "\nResult:", R )
