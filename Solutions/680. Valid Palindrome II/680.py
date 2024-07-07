class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(p1 : int, p2 : int,  hasIgnored: int) -> bool:
            if hasIgnored > 1:
                return False
            while p1 < p2:
                if s[p1] == s[p2]:
                    p1 += 1
                    p2 -= 1 
                else: 
                    return isPalindrome(p1 + 1, p2, hasIgnored + 1) or isPalindrome(p1, p2 - 1, hasIgnored + 1)
            return True
        return isPalindrome(0, len(s) - 1, 0)
        