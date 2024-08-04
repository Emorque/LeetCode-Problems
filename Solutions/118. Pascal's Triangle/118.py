from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        output = [[1], [1,1]]
        for i in range(2, numRows):
            newList = [1] * (i + 1)
            for j in range(1, len(newList) - 1):
                newList[j] = output[i-1][j] + output[i-1][j-1]
            output.append(newList)
        return output