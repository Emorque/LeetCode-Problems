class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        traversing = False
        hashmap = {}
        s1Length = len(s1)

        for char in s1:
            hashmap[char] = 1 + hashmap.get(char, 0)
            
        for i, char in enumerate(s2):
            if traversing:
                if char in hashmap and hashmap[char] == 1 and (i - left + 1) == s1Length:
                    return True
                if char not in hashmap:
                    while left != i:
                        hashmap[s2[left]] += 1
                        left += 1
                    traversing = False
                elif hashmap[char] == 0:
                    while s2[left] != char:
                        hashmap[s2[left]] += 1
                        left += 1
                    left += 1
                else:
                    hashmap[char] -= 1
            elif char in hashmap:
                left = i 
                hashmap[char] -= 1
                traversing = True
                if (i - left + 1) == s1Length:
                    return True
        return False