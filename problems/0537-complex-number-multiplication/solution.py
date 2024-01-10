class Solution:
    def str_to_num(self, num):
        split = num.split('+')
        return int(split[0]), int(split[1][:-1])

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = self.str_to_num(num1)
        c, d = self.str_to_num(num2)
        return f"{a*c - b*d}+{a*d + b*c}i"
