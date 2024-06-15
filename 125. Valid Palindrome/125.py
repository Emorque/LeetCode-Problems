class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
    
        p1 = 0
        p2 = len(s) - 1

        while (p1 <= p2):
            while (not (s[p1].isalnum())):
                if (p1 >= p2):
                    return True
                p1 += 1
            while (not (s[p2].isalnum())):
                p2 -= 1
            if (s[p1].lower() != s[p2].lower()):
                return False
            p1 += 1
            p2 -= 1
        return True