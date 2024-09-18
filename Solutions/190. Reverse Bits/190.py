class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            bit = n & 1
            
            output = output << 1
            output = output | bit

            n = n >> 1            
        return output