class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        if x >= 0:
            bound = (2 ** 31) - 1
        else:
            bound = 2 ** 31
        
        x = abs(x)
        output = 0

        while x != 0:
            if output * 10 > bound:
                return 0
            output *= 10
            output += x % 10
            x = x //10

        return output * (-1) if negative else output