from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target1 = target[0]
        target2 = target[1]
        target3 = target[2]

        t1Found = False
        t2Found = False
        t3Found = False

        for i, j, k in triplets:
            if t1Found and t2Found and t3Found:
                return True
            if i > target1 or j > target2 or k > target3:
                continue
            if i == target1:
                t1Found = True
            if j == target2:
                t2Found = True
            if k == target3:
                t3Found = True
        
        return t1Found and t2Found and t3Found