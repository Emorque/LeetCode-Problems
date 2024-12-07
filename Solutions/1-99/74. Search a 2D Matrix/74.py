from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                #valid row
                row = mid
                low, high = 0, len(matrix[0]) - 1
                while low <= high:
                    mid = low + (high - low) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
            elif matrix[mid][0] < target:
                low = mid + 1
            else: 
                high = mid - 1
        return False