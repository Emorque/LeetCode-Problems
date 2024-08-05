from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            prev: int = row[0]
            for j in range(1, i):
                temp: int = row[j]
                row[j] = row[j] + prev
                prev = temp
        return row