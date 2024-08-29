1. Share questions you would ask to help understand the question:
- Are there unique values between both arrays?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Binary Search (Likely)
- Sorting (Neutral) 

3. Write out in plain English what you want to do: 
- The really easy way to go about this is to join the two arrays together, sort them, and then return the median depending on total array length
- However, the constraint on having this be O(log(m + n)) makes this tricky 
- Log(m + n) makes me think immediately of a binary search like algorithm 
- There seems to be some unique test cases already 
  - ex 1: [1, 3] [2 ] 
    - The numbers of one list can be considered within the range of the other list 
  - ex 2: [1, 2] [3, 4]
    - The numbers considered for the median (even) has to be calculating based on the edges of lists
- A median means the number that splits an array into 2 halves
- Since joining and sorting is out of the picture, getting the length of that half is important 
- So by getting the len of the two arrays, and then dividing by 2, the length of half is calcualted
- Using that half, now I need to get the number of numbers that are a count of half. So if half is 2, I need the smallest 2 numbers between both arrays 
- To just have something, the smaller of the two lists can be used
  - It can be split in half using binary search: low, high, mid
  - The distance between low and mid will be the left side of that array. To get the left side of the other array, that can be done by doing half - leftside distance of the first array 
- Now, maybe there is a chance that both rightmost numbers of the leftsides are less than the opposing leftmost element of the right side of the other array. 
  - If that is the case, then depending on even/odd total array length, get the median 
- However, if one of the numbers are not less than the rightmost .... of the other array, 
  - Then the low/high elements have to be adjusted to mid like traditional binary search 

4. Translate each sub-problem into pseudocode:
- Skipped because 3. is kind of like psuedocode 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
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
                low = mid + 1  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that binary search is used to determine the halfs of the arrays, and which is much better than starting from 0, and then linearly increasing halves by 1 
- One weak area is that this problem can be hard to understand. I could take some comments from 3. and put them here. Also renaming the variables would help, I got a bit lost myself with them. 