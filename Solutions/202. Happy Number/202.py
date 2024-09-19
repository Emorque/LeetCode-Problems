class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            happy = 0
            while n != 0:
                happy += ((n % 10) ** 2)
                n = n // 10
            n = happy
        return True