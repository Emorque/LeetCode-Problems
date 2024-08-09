from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output: List[List[str]] = []
        output.append([strs[0]])
        for i in range(1, len(strs)):
            currStr = strs[i]
            found = 0
            for strList in output:
                firstStr = strList[0]
                if len(firstStr) != len(currStr):
                    continue
                hashmap = {}
                temp = 0
                for char in firstStr:
                    if char not in hashmap:
                        hashmap[char] = 0
                    hashmap[char] += 1
                for char in currStr:
                    if char not in hashmap:
                        temp = 1
                        break
                    hashmap[char] -= 1
                if temp == 1: 
                    continue
                for value in hashmap.values():
                    if value != 0: 
                        temp = 1
                        break
                if temp == 1: 
                    continue
                strList.append(currStr)    
                found = 1
                break
            if found != 1:
                output.append([currStr])

        return output