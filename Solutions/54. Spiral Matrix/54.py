from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        output : List[int] = []

        def helper(row: int, column: int, layer: int):
            if layer >= row/2 and layer >= column/2:
                output.append(matrix[row//2][column//2])
                return

            if len(output) > row * column:
                return

            for i in range(layer, column - layer - 1):
                output.append(matrix[layer][i])

            for j in range(layer, row - layer - 1):
                output.append(matrix[j][column - layer - 1])

            for h in range(column - layer - 1, layer, -1):
                output.append(matrix[row - layer - 1][h])

            for k in range(row - layer - 1, layer, -1):
                output.append(matrix[k][layer])

            if not len(output) == row * column:
                helper(row, column, layer + 1)
                
        helper(len(matrix), len(matrix[0]), 0)
        while len(output) > len(matrix) * len(matrix[0]):
            output.pop()
        return output
