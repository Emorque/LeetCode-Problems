class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        length = float("inf")
        if t == "": 
            return res

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT) # countT has the number of unique characters in t
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update the res if it is smaller than my current res
                if r - l + 1 < length:
                    length = r - l + 1
                    res = s[l:r+1]

                # pop frrom the left of the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        return res
        
        
        # res = ""
        # length = float("inf")

        # traversing = False
        # left = 0

        # freq = {}
        # for char in t:
        #     freq[char] = freq.get(char, 0) + 1
        
        # def completedT():
        #     for v in freq.values():
        #         if v > 0:
        #             return False
        #     return True

        # for right in range(len(s)):
        #     if traversing:
        #         if s[right] not in freq:
        #             continue
        #         elif freq[s[right]] > 0:
        #             s[right] -= 1
        #             if s[right] == 0 and completedT():
        #                 if right - left + 1 < length:
        #                     length = right - left + 1
        #                     res = s[left:right+1]
        #         if freq[s[right]] < 0:
        #             if freq[s[left]] < 0:

                    
        #         continue
            
        #     elif s[right] in freq:
        #         pass
        #         freq[s[right]] -= 1
        #         if len(t) == 1:
        #             return s[right]
        #         left = right
        #         traversing = True
        
        # return res