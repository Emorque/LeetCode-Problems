class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        if n > 0:
            positive = True
        else:
            positive = False

        halfPower = self.myPow(x, abs(n)//2)
        answer = halfPower * halfPower
        
        if n % 2 == 1:
            answer *= x
        
        return answer if positive else 1/answer


#HELPER FUNCTIOn
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            halfPower = helper(x, abs(n)//2)
            answer = halfPower * halfPower

            if n % 2 == 1:
                answer *= x

            return answer

        if n > 0:
            positive = True
        else:
            positive = False

        return helper(x,n) if positive else 1/helper(x,abs(n))

        