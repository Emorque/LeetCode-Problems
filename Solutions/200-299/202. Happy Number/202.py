class Solution:
    def isHappy(self, n: int) -> bool:
        def getHappy(num: int) -> int:
            happy = 0
            while num != 0:
                happy += ((num % 10) ** 2)
                num = num // 10
            return happy
        
        slow, fast = n, n
        while fast != 1:
            slow = getHappy(slow)
            fast = getHappy(getHappy(fast))
            if slow == fast and fast != 1:
                return False
        return True