from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left, right = 0, 0
        output = []
        count = 0

        continueRight = False

        charFreq = {}

        for char in s:
            charFreq[char] = 1 + charFreq.get(char, 0)
        
        while right < len(s):
            while charFreq[s[left]] != 0:
                charFreq[s[right]] -= 1
                right += 1
                count += 1
            if right == len(s):
                break
            while left != right:
                if charFreq[s[left]] != 0:
                    continueRight = True
                    break
                left += 1
            if continueRight:
                continueRight = False
                continue
            output.append(count)
            count = 0
        
        output.append(count)

        return output