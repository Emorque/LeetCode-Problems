from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minAndMax = set()
        output = []
        # get the mins
        for i in range(len(matrix)):
            minimum = 1000000
            for j in range(len(matrix[i])):
                minimum = min(minimum, matrix[i][j])
            minAndMax.add(minimum)
        #get the maxes
        for i in range(len(matrix[i])):
            maximum = 0
            for j in range (len(matrix)):
                maximum = max(maximum, matrix[j][i])
            if maximum in minAndMax:
                output.append(maximum)
        return output