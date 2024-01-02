class Solution:
    def sum(self, num1: int, num2: int) -> int:
        if num1 >= 0 and num2 >= 0:
            return self.add(num1, num2)
        elif num1 < 0 and num2 < 0:
            return -1 * self.add(-1 * num1, -1 * num2)
        elif num1 < 0:
            return (-1 if -1 * num1 > num2 else 1) * self.sub(
                *sorted([-1 * num1, num2], reverse=True)
            )
        elif num2 < 0:
            return (-1 if -1 * num2 > num1 else 1) * self.sub(
                *sorted([num1, -1 * num2], reverse=True)
            )

    def add(self, num1: int, num2: int) -> int:
        carry, ans, d = 0, 0, 0
        while num1 > 0 or num2 > 0 or carry:
            s = num1 % 10 + num2 % 10 + carry
            if s >= 10:
                carry = 1
                s = s % 10
            else:
                carry = 0
            ans = s * 10**d + ans
            num1 //= 10
            num2 //= 10
            d += 1
        return ans

    def sub(self, num1: int, num2: int) -> int:
        borrow, ans, d = 0, 0, 0
        while num1 > 0 or borrow > 0:
            d1, d2 = num1 % 10, num2 % 10
            d1 -= borrow
            borrow = 0
            if d1 < d2:
                d1 += 10
                borrow = 1
            diff = d1 - d2
            ans = diff * 10**d + ans
            num1 //= 10
            num2 //= 10
            d += 1
        return ans

