from typing import List

def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        hashMap = {}
        for p1, p2 in trust:
            if p1 not in hashMap:
                hashMap[p1] = 0
            if p2 not in hashMap:
                hashMap[p2] = 0
            hashMap[p1] -= 1
            hashMap[p2] += 1
        for person in hashMap:
            if hashMap[person] == n - 1: return person
        return -1