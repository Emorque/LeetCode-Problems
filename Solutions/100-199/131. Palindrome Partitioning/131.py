class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(substring: str) -> bool:
            left,right = 0, len(substring) - 1

            while left < right:
                if substring[left] != substring[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        partitions = []
        palindromes = []

        def helper(substring):
            if len(substring) == 0:
                partitions.append(palindromes[:])
                return
        
            for i in range(len(substring)):    
                if isPalindrome(substring[:i + 1]):
                    palindromes.append(substring[:i + 1])
                    helper(substring[i + 1:])
                    palindromes.pop()
        
        helper(s)
        return partitions