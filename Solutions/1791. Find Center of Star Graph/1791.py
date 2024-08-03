from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n1, n2, n3, n4 = edges[0][0], edges[0][1], edges[1][0], edges[1][1]
        return n1 if n1 == n3 or n1 == n4 else n2