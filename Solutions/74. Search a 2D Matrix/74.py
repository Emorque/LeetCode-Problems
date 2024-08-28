from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] == target: 
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        # current row is high 
        
        l, h = 0, len(matrix[high]) - 1

        while l <= h:
            mid = l + (h - l) // 2

            if matrix[high][mid] == target: 
                return True
            elif matrix[high][mid] < target:
                l = mid + 1
            else: 
                h = mid - 1
        return False