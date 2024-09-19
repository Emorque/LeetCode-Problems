from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        layer = len(matrix) // 2
        swaps = len(matrix) - 1
        edge = len(matrix) - 1 

        for i in range(layer):
            for j in range(swaps):
                topL = matrix[i][i + j]
                topR = matrix[i + j][edge]
                bottomR = matrix[edge][edge - j]
                bottomL = matrix[edge - j][i]

                matrix[i][i + j] = bottomL
                matrix[i + j][edge] = topL
                matrix[edge][edge - j] = topR
                matrix[edge - j][i] = bottomR

            edge -= 1
            swaps -= 2