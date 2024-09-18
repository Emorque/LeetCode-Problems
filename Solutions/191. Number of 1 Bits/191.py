class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            newN = n >> 1
            if n == (newN * 2) + 1:
                count += 1
            n = newN
        return count
    
#Simplier solution:
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count