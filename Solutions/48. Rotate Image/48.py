from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper(length:int, layer:int):
            print(matrix)
            if layer >= length/2:
                return
            for i in range(layer, length - 1 - layer):
                a : int = matrix[layer][i]
                b : int = matrix[i][length - 1 - layer]
                c : int = matrix[length - 1 - layer][length - 1 - i]
                d : int = matrix[length - 1- i][layer]

                matrix[layer][i] = d
                matrix[i][length - 1 - layer] = a
                matrix[length - 1 - layer][length - 1 - i] = b
                matrix[length - 1- i][layer] = c
            helper(length, layer + 1)
        helper(len(matrix), 0)
        return
                