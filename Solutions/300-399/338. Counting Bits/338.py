from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % 2 == 1:
                output[i] = output[i - 1] + 1
            else:
                output[i] = output[i // 2]
        return output