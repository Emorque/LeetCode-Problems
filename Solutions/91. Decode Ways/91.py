class Solution:
    def numDecodings(self, s: str) -> int:
        decodings = {len(s) : 1}
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                decodings[i] = 0
            else:
                decodings[i] = decodings[i + 1]
            
            if i < (len(s) - 1) and (s[i] == "1" or (s[i] ==  "2" and s[i + 1] in "0123456")):
                decodings[i] += decodings[i + 2]
        return decodings[0]
            

