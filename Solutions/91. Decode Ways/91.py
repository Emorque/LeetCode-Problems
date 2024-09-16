class Solution:
    def numDecodings(self, s: str) -> int:
        decodings = {} 
        decodings[len(s)] = 1

        def traverse(index):
            if index in decodings:
                return decodings[index]
            if s[index] == "0":
                return 0
            
            decodeNo = traverse(index + 1)
            if index < len(s) - 1 and (s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456")):
                decodeNo += traverse(index + 2)
            decodings[index] = decodeNo
            return decodeNo
        return traverse(0)