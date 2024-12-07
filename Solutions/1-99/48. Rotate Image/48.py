from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                a = matrix[left][left + i]
                b = matrix[left + i][right]
                c = matrix[right][right - i]
                d = matrix[right - i][left]
            
                matrix[left][left + i] = d
                matrix[left + i][right] = a
                matrix[right][right - i] = b
                matrix[right - i][left] = c

            left += 1
            right -= 1