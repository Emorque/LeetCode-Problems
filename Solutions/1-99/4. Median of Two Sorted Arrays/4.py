from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        s, l = nums1, nums2 

        if len(s) > len(l):
            s, l = l, s
        
        low, high = 0, len(s) - 1
        while True: 
            mid = low + (high - low) // 2
            lHalf = half - mid - 2

            # left half, right half
            sLeft = s[mid] if mid >= 0  else (10 ** 6) * -1
            sRight = s[mid + 1] if mid < len(s) - 1 else (10 ** 6) 

            lLeft = l[lHalf] if lHalf >= 0  else (10 ** 6) * -1
            lRight = l[lHalf + 1] if lHalf < len(l) - 1 else (10 ** 6)

            # binary search conditions  
            if sLeft <= lRight and lLeft <= sRight:
                if total % 2 == 0:
                    return (max(sLeft, lLeft) + min(sRight, lRight)) / 2
                return min(sRight, lRight)
            elif sLeft > lRight:
                high = mid - 1
            else: 
                low = mid + 1