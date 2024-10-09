from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        end = len(nums1) - 1

        while end >= 0:
            if p2 < 0:
                return
            if p1 < 0:
                nums1[end] = nums2[p2]
                p2 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[end] = nums1[p1]
                nums1[p1] = nums2[p2]
                p1 -= 1
            else:
                nums1[end] = nums2[p2]
                nums2[p2] = 0
                p2 -= 1
            end -= 1
        