from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output: List[List[int]] = []

        for i in range(len(matrix[0])):
            entry : List[int] = []
            for j in range(len(matrix)):
                entry.append(matrix[j][i])
            output.append(entry)
        return output