from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        for i, char  in enumerate(s):
            if char == c:
                answer.append(0)
            else:
                p1 = p2 = i
                count = 0
                while (p1 != 0 or p2 != len(s) - 1):
                    if p1 != 0:
                        p1 -= 1
                    if p2 != len(s) - 1:
                        p2 += 1
                    count += 1
                    if (s[p1] == c or s[p2] == c):
                        break
                answer.append(count)
        return answer